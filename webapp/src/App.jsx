import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
  RouterProvider,
} from "react-router-dom";

import React from "react";
import HomePage from "./pages/HomePage";
import WipPage from "./pages/WipPage";
import PreviousEntriesPage from "./pages/PreviousEntriesPage";
import MainLayout from "./layouts/MainLayout";

const App = () => {
  const name = "Edward";

  const addEntry = async (newEntry) => {
    console.log(newEntry);
  };

  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path="/" element={<MainLayout />}>
        <Route index element={<HomePage />} />
        <Route path="/previous-entries" element={<PreviousEntriesPage />} />
        <Route path="/trends" element={<WipPage />} />
        <Route path="*" element={<WipPage />} />
      </Route>
    )
  );

  return <RouterProvider router={router} />;
};

export default App;
