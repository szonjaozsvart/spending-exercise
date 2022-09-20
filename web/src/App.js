import React, { useState } from "react";
import Form from "./components/Form";
import FiltersAndOrderings from "./components/FiltersAndOrderings";
import SpendingList from "./components/SpendingList";
import Layout from "./components/Layout";

export default function App() {
  const [spendings, setSpendings] = useState([]);
  const [sortBy, setSortBy] = useState("-date");
  const [currencyBy, setCurrencyBy] = useState("ALL");

  return (
    <>
      <Layout>
        <Form />
        <FiltersAndOrderings
          currencyBy={currencyBy}
          setCurrencyBy={setCurrencyBy}
          sortBy={sortBy}
          setSortBy={setSortBy}
        />
        <SpendingList
          spendings={spendings}
          setSpendings={setSpendings}
          currencyBy={currencyBy}
          sortBy={sortBy}
        />
      </Layout>
    </>
  );
}
