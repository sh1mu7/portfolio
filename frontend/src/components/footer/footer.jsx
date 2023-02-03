import React, { useContext } from "react";
import { DarkModeContext } from "../../DarkModeContext";
import NavItems from "../nav/navItems";

function Footer({ setNavLinks, setBar }) {
  const { darkMode } = useContext(DarkModeContext);
  return (
    <div className="footer_main">
      <div className="copy-right">
        <p className={darkMode ? "dark" : ""}>
          Copyright &#169; 2022, Nittanando Sarkar.
        </p>
      </div>
      <div className="footer-nav">
        <ul className="">
          <NavItems setNavLinks={setNavLinks} setBar={setBar}/>
        </ul>
      </div>
    </div>
  );
}

export default Footer;
