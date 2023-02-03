import { useContext } from "react";
import { NavLink } from "react-router-dom";
import { DarkModeContext } from "../../DarkModeContext";
import { Navdata } from "../data/navData";

function NavItems({ setNavLinks, setBar }) {
 
  const { darkMode } = useContext(DarkModeContext);
 
  const handleClick = () => {
    setNavLinks(false)
    setBar(false)
  }

  return (
    <>
      {Navdata.map((item, index) => {
        return (
          <li key={index}>
            <NavLink
            onClick={handleClick}
              className={({ isActive }) => {
                return (
                  `nav-links ${
                    darkMode ? " navLInkdark nav-links-dark " : ""
                  }` + (isActive ? "n-active" : "")
                );
              }}
              to={`${item.url}`}
            >
              {item.title}
            </NavLink>
          </li>
        );
      })}
    </>
  );
}

export default NavItems;
