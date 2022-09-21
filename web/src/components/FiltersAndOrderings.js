import React from "react";
import {
  FiltersWrapper,
  Orderings,
  CurrencyFilters,
  CurrencyButton,
} from "../styles/ComponentStyles";

export default function CurrencyFilter({
  currencyBy,
  setCurrencyBy,
  setSortBy,
}) {
  return (
    <>
      <FiltersWrapper>
        <Orderings>
          <select onChange={(e) => setSortBy(e.currentTarget.value)}>
            <option value="-date">Sort by Date descending (default)</option>
            <option value="date">Sort by Date ascending</option>
            <option value="-amount_in_huf">Sort by Amount descending</option>
            <option value="amount_in_huf">Sort by Amount ascending</option>
          </select>
        </Orderings>
        <CurrencyFilters>
          <li>
            <CurrencyButton
              name=""
              style={{
                backgroundColor: currencyBy === "ALL" ? "lightGrey" : "white",
              }}
              onClick={() => setCurrencyBy("ALL")}
            >
              ALL
            </CurrencyButton>
          </li>
          <li>
            <CurrencyButton
              name="HUF"
              style={{
                backgroundColor: currencyBy === "HUF" ? "lightGrey" : "white",
              }}
              onClick={() => setCurrencyBy("HUF")}
            >
              HUF
            </CurrencyButton>
          </li>
          <li>
            <CurrencyButton
              name="USD"
              style={{
                backgroundColor: currencyBy === "USD" ? "lightGrey" : "white",
              }}
              onClick={() => setCurrencyBy("USD")}
            >
              USD
            </CurrencyButton>
          </li>
        </CurrencyFilters>
      </FiltersWrapper>
    </>
  );
}
