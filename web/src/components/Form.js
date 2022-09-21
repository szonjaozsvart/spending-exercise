import React, { useState } from "react";
import { InputStyles } from "../styles/InputStyles";
import { SelectStyles } from "../styles/SelectStyles";
import { FormStyles, ErrorMessage } from "../styles/ComponentStyles";

export default function Form() {
  const [error, setError] = useState(false);
  const [state, setState] = useState({
    description: "",
    amount: 0,
    currency: "USD",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("/spendings", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        description: state.description,
        amount: state.amount,
        currency: state.currency,
      }),
    });
    if (response.status !== 200) {
      setError(true);
      return;
    }
    const body = await response.json();
    setError(false);
    window.location.reload();
    setState({
      description: "",
      amount: 0,
      currency: "USD",
    });
  };

  function handleChange(e) {
    const { name, value } = e.target;

    setState({
      ...state,
      [name]: value,
    });
  }

  return (
    <>
      {error && (
        <ErrorMessage>
          Please fill the description and the amount as well!
        </ErrorMessage>
      )}
      <FormStyles onSubmit={handleSubmit}>
        <InputStyles
          type="text"
          placeholder="description"
          name="description"
          value={state.description}
          onChange={handleChange}
        />
        <InputStyles
          type="number"
          placeholder="amount"
          name="amount"
          value={state.amount}
          onChange={handleChange}
        />
        <SelectStyles
          name="currency"
          value={state.currency}
          onChange={handleChange}
        >
          <option value="HUF">HUF</option>
          <option value="USD">USD</option>
        </SelectStyles>
        <InputStyles type="submit" value="Save" />
      </FormStyles>
    </>
  );
}
