import React, { useState, useEffect } from "react";
import { FiDollarSign } from "react-icons/fi";
import { DateTime } from "luxon";
import Loader from "./Loader";
import {
  ErrorMessage,
  Spending,
  IconWrapper,
  TextWrapper,
  Amount,
  AmountWrapper,
} from "../styles/ComponentStyles";
import { ImCross } from "react-icons/im";
import { HiOutlinePencil } from "react-icons/hi";

export default function SpendingList({
  spendings,
  setSpendings,
  currencyBy,
  sortBy,
}) {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    setLoading(true);
    console.log(sortBy, currencyBy);
    fetch(`/spendings?currency=${currencyBy}&order=${sortBy}`, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then(async (res) => {
        console.log("visszajön");
        const body = await res.json();
        return {
          status: res.status,
          body,
        };
      })
      .then((response) => {
        if (response.status === 200) {
          setSpendings(response.body);
        }
      })
      .catch((err) => {
        console.error(err);
        setError(true);
      })
      .finally(() => {
        setLoading(false);
      });
  }, [currencyBy, sortBy]);

  if (loading) return <Loader />;

  return (
    <>
      {error && (
        <ErrorMessage>
          The server is probably down. Please try again later.
        </ErrorMessage>
      )}
      {!spendings.length && !error && (
        <h1 style={{ textAlign: "center", marginTop: "4rem" }}>
          Yay!{" "}
          <span role="img" aria-label="jsx-a11y/accessible-emoji">
            🎉
          </span>{" "}
          No spendings!
        </h1>
      )}
      {spendings.length > 0 &&
        spendings.map((spending) => (
          <Spending key={spending.id}>
            <IconWrapper>
              <FiDollarSign color="var(--color-blue)" />
            </IconWrapper>
            <TextWrapper>
              <h3>{spending.description}</h3>
              <p>
                {DateTime.fromISO(spending.spent_at).toFormat(
                  "t - MMMM dd, yyyy"
                )}
              </p>
            </TextWrapper>
            <AmountWrapper>
              <Amount currency={spending.currency}>
                {(spending.amount / 100).toFixed(2)}
              </Amount>
            </AmountWrapper>
            <div className="update">
              <button className="update-btn">
                <HiOutlinePencil />
              </button>
            </div>
            <div className="delete">
              <button className="del-btn">
                <ImCross />
              </button>
            </div>
          </Spending>
        ))}
    </>
  );
}
