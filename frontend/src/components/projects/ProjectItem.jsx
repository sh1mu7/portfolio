import React, { useContext } from "react";
// import Roy from "../../asset/image/roy.png"

import { Link } from "react-router-dom";
import { DarkModeContext } from "../../DarkModeContext";

function ProjectItem({ item }) {
  const { darkMode } = useContext(DarkModeContext);

  return (
    <div className="project">
      <i
        className={`fa-solid fa-diagram-project ${darkMode ? "dark" : ""}`}
      ></i>
      <div className="project-detail">
        <Link className={darkMode ? "dark" : ""} to={`/projects/${item.id}`}>
          <h3>{item.title}</h3>
        </Link>

        <p className={darkMode ? "dark" : ""}>{item.description}</p>
      </div>
    </div>
  );
}

export default ProjectItem;

// <>
//       {ProjectData.map((item, index) => {
//         return (
//           <div key={index} className="project">
//             <i
//               className={`fa-solid fa-diagram-project ${
//                 darkMode ? "dark" : ""
//               }`}
//             ></i>
//             <div className="project-detail">
//               <Link className={darkMode ? "dark" : ""} to={item.url}>
//                 <h3>{item.title}</h3>
//               </Link>
//               <p className={darkMode ? "dark" : ""}>{item.description}</p>
//             </div>
//           </div>
//         );
//       })}
//     </>
