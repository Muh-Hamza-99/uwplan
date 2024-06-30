import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import About from "./pages/About";
import Me from "./pages/Me";

import Footer from "./components/Footer";

const App = () => {
  return (
    <>
      <div className="min-h-screen">
        <Router>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/me" element={<Me />} />            
          </Routes>
        </Router>
      </div>
      <Footer />
    </>
  );
};

export default App;
