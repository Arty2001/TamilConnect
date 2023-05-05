import React from 'react';
import { NavbarMinimal } from './component/NavbarMinimal';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import {Home} from "./pages/Home";
import { FindPage } from "./pages/FindPage";
import { SearchPage } from "./pages/SearchPage";
import { Group } from '@mantine/core';

function App() {
  return (
    <div className="App">
      <Group>
      <BrowserRouter>
        <NavbarMinimal />
        <Routes>
          <Route path="Home" element={<Home />} />
          <Route path="FindPage" element={<FindPage />} />
          <Route path="SearchPage" element={<SearchPage />} />
        </Routes>
      </BrowserRouter>
      </Group>
    </div>
  );
}

export default App;
