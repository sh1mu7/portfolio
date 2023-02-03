import { useContext } from "react";
import { useParams } from "react-router-dom";
import { DarkModeContext } from "../../DarkModeContext";
import { ProjectData } from "../data/projectData";

function ProjectSingle() {
  const { id } = useParams();
  const project = ProjectData.find((item) => item.id === id);
  const { darkMode } = useContext(DarkModeContext);
  const handleDark = () => {
    return darkMode ? "dark" : "";
  };
  return (
    <div className="project-single-main">
      <div className="project-single-wrapper">
        <h1 className={handleDark()}>{project.title}</h1>
        <p className={handleDark()}>{project.description}</p>
        <h3 className={handleDark()}>Functionality</h3>
        <p className={handleDark()}>{project.functionality}</p>
        <a className={handleDark()} href={project.url} target="blank">
          Click to see live project
        </a>
      </div>
    </div>
  );
}

export default ProjectSingle;
