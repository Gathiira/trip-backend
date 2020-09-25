import React, { useMemo, useState, useEffect } from "react";

import Table from "./Table";
import "../App.css";

import { ApiCall } from './ApiCall';


function TripsTable() {
  const columns = useMemo(
    () => [
      {
        Header: "Name",
        accessor: "title",
      },
      {
        Header: "Loading Details",
        columns: [

          {
            Header: "Departure Date",
            accessor: "departure_date",
          },
          {
            Header: "Buying Price/KG",
            accessor: "buying_price_per_kg"
          },
          {
            Header: "Total Weight Bought",
            accessor: "total_weight_bought"
          },
          {
            Header: "Total Buying Price",
            accessor: "total_buying_price"
          },
          {
            Header: "Loading cost",
            accessor: "loading_cost"
          }
        ]
      },
      {
        Header: "Additional Costs",
        columns: [
          {
            Header: "Transport cost",
            accessor: "trip_offloading.transport_cost"
          },
          {
            Header: "Clearance cost",
            accessor: "trip_offloading.clearance_cost"
          },
        ]
      },
      {
        Header: "Offloading Details",
        columns: [
          {
            Header: "Selling Date",
            accessor: "trip_offloading.selling_date"
          },
          {
            Header: "Selling Price/KG",
            accessor: "trip_offloading.selling_price_per_kg"
          },
          {
            Header: "Total Weight sold",
            accessor: "trip_offloading.total_weight_sold",
          },
          {
            Header: "Total Selling Price",
            accessor: "trip_offloading.total_selling_price",
          },
          {
            Header: "Offloading Cost",
            accessor: "trip_offloading.offloading_cost",
          },
          {
            Header: "Broker Expense",
            accessor: "trip_offloading.broker_expenses",
          },
          {
            Header: "Total Expenses",
            accessor: "trip_offloading.total_expenses",
          },
        ]
      },
      {
        Header: "Profit Margin",
        accessor: "trip_offloading.profit_margin"
      },
    ],
    []
  );

  const [data, setData] = useState([]);

  useEffect(() => {
    ApiCall("loading/",'').then((result) =>{
      let responseJson = result;
      setData(responseJson.data);
    })
  }, []);

  return (
    <>
    <div className="m-auto">
      <div className='card card-body mt-5'>
        <div className='text-center'><h2>Information Center</h2></div>
        <div id='table_data'>
          <Table columns={columns} data={data} />
        </div>
      </div>
    </div>
    </>
  );
}

export default TripsTable;
