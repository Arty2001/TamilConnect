import React from 'react';
import { HeaderTabs } from './component/HeaderTabs';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Home } from "./pages/Home";
import  FindPage  from "./pages/FindPage";
import { Recipes } from "./pages/Recipes";
import { Flex, MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider theme={{
      fontFamily: 'Open Sans, sans-serif'}
    } withGlobalStyles withNormalizeCSS>
      <div className="App">
          <BrowserRouter>
            <HeaderTabs user={{ name: "JoeRex", image: "data:image/png;base64,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" }} tabs={["Home", "Grocery Finder", "Recipe Finder"]}/>
            <Routes>
              <Route path="Home" element={<Home />} />
              <Route path="Grocery Finder" element={<FindPage />} />
              <Route path="Recipe Finder" element={<Recipes />} />
            </Routes>
          </BrowserRouter>
      </div>
    </MantineProvider>
  );
}

export default App;
