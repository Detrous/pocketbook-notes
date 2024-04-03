import { Routes, Route } from "react-router-dom";

import Words from "../pages/Words";
import Books from "../pages/Books";
import BaseLayout from "../layouts/default/BaseLayout";

const Router = () => {
  return (
    <BaseLayout>
      <Routes>
        <Route path="/words" element={<Words />} />
        <Route path="/books" element={<Books />} />
      </Routes>
    </BaseLayout>
  );
};
export default Router;
