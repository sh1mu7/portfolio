import React, { useContext } from "react";
import { Link } from "react-router-dom";
import darkLogo from "../../asset/image/logo-dark.svg";
import logo from "../../asset/image/s.svg";
import { DarkModeContext } from "../../DarkModeContext";
import Routing from "../router/Routing";
import NavItems from "./navItems";


function Navbar({ setNavLinks, setBar, bar, navLinks }) {
  // const [bar, setBar] = useState(false);
  // const [navLinks, setNavLinks] = useState(false);

  const { darkMode, toggleDarkMode } = useContext(DarkModeContext);

  function handleClickBar() {
    setBar((bar) => !bar);
    setNavLinks((navLinks) => !navLinks);
  }

  let toggleBar = bar ? " fas fa-times" : " fa-solid fa-bars";
  let toggleBarContent = navLinks ? "nav-ul-show" : "nav-ul-hide";

  return (
    <>
      <nav className="navbar_main">
        <div className="nav-secondary-wrapper">
          
          <Link className="logo-wrap" to="/">
          <img
            className={`logo ${darkMode ? "d-block " : "d-none"}`}
            src={darkLogo}
            alt="logo"
          />
          <img
            className={`logo ${darkMode ? "d-none " : "d-block"}`}
            src={logo}
            alt="logo"
          />
          </Link>
          <div className="nav-link-wrapper">
            <Link className="title-wrap" to="/"><h2 className={darkMode ? "dark" : ""}>sh1mu7</h2></Link>
            <ul className={`${toggleBarContent} ${darkMode ? " dark-ul" : ""}`}>
              <NavItems setNavLinks={setNavLinks} setBar={setBar} />
            </ul>
          </div>
        </div>

        <i
          onClick={toggleDarkMode}
          className={`fa-solid fa-moon light ${darkMode ? "dark" : ""}`}
          id="dark"
        ></i>
        <i
          onClick={handleClickBar}
          className={`menu ${toggleBar} ${darkMode ? " dark" : ""}`}
        ></i>
      </nav>
     <Routing/>
    </>
  );
}

export default Navbar;

