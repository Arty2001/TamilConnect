import React from 'react';
import { NavbarMinimal } from './component/NavbarMinimal';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Home } from "./pages/Home";
import { FindPage } from "./pages/FindPage";
import { Recipes } from "./pages/Recipes";
import { Flex, MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider withGlobalStyles withNormalizeCSS>
      <div className="App">
        <Flex align="center">
          <BrowserRouter>
            <NavbarMinimal />
            <Routes>
              <Route path="Home" element={<Home />} />
              <Route path="FindPage" element={<FindPage />} />
              <Route path="Recipes" element={<Recipes />} />
            </Routes>
          </BrowserRouter>
        </Flex>
      </div>
    </MantineProvider>
  );
}

export default App;
