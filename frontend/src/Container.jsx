import React, { useContext, useState } from "react";
import Footer from "./components/footer/footer";
import Navbar from "./components/nav/navbar";
import { DarkModeContext } from "./DarkModeContext";

function Container() {
  const { darkMode } = useContext(DarkModeContext);
  const [bar, setBar] = useState(false);
  const [navLinks, setNavLinks] = useState(false);
  return (
    <div className={`main_app-wrapper ${darkMode ? "lightMode" : ""}`}>
      <div className="main_app">
        <Navbar bar={bar} setBar={setBar} navLinks={navLinks} setNavLinks={setNavLinks}/>

        <Footer bar={bar} setBar={setBar} navLinks={navLinks} setNavLinks={setNavLinks}/>
      </div>
    </div>
  );
}

export default Container;
