import React, { useContext } from "react";
import { DarkModeContext } from "../../DarkModeContext";
import { ProjectData } from "../data/projectData";
import ProjectItem from "./ProjectItem";

function Project() {
  const { darkMode } = useContext(DarkModeContext);
  return (
    <div className="project_main">
      <div className="project_main-inner">
        <h2 className={darkMode ? "dark" : ""}>Projects</h2>

        <div className="projects-wrapper">
          {ProjectData.map((item, index) => {
            return <ProjectItem key={index} item={item}/>;
          })}
        </div>
      </div>
    </div>
  );
}

export default Project;
