import React, {useContext} from "react";
import {DarkModeContext} from "../../DarkModeContext";
import {AboutData} from "../data/AboutData";
import Education from "./Education";
// import CV from "../../asset/cv/Nittanando.pdf";



function About() {
    const {darkMode} = useContext(DarkModeContext);
    const toggleDark = () => {
        return darkMode ? "dark" : "";
    };

    const onButtonClick = () => {
        // using Java Script method to get PDF file
        fetch("Nittanando.pdf").then((response) => {
            response.blob().then((blob) => {
                // Creating new object of PDF file
                const fileURL = window.URL.createObjectURL(blob);
                // Setting various property values
                let alink = document.createElement("a");
                alink.href = fileURL;
                alink.download = "Nittanando.pdf";
                alink.click();
            });
        });
    };
    return (
        <div className="about_main">
            <div className="about-me">
                <h2 className={toggleDark()}>About me</h2>
                <p className={toggleDark()}>
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eius a
                    aliquam iste eum assumenda quis, architecto neque suscipit,
                    laboriosam, impedit culpa ab accusantium illum? Corrupti, dignissimos.
                    Ipsum reprehenderit minus, cumque dolor nostrum mollitia amet
                    blanditiis nulla animi doloribus enim quae! Lorem ipsum, dolor sit
                    amet consectetur adipisicing elit. Ipsa sapiente vero illum, deleniti
                    sint voluptas in consectetur laboriosam doloribus! Iusto.
                </p>
            </div>
            <div className="skills">
                <h2 className={toggleDark()}>Education</h2>
                {AboutData.map((item, index) => {
                    return (
                        <Education
                            key={index}
                            institute={item.institute}
                            certificate={item.certificate}
                            session={item.session}
                        />
                    );
                })}
            </div>
            <div className="skills">
                <h2 className={toggleDark()}>Skills</h2>
                <div className="skills-main">
                    <h3 className={toggleDark()}>Markup and Styling</h3>
                    <div className="skill-sub">
                        <i class={`fa-solid fa-arrow-turn-up ${toggleDark()}`}></i>
                        <p className={toggleDark()}>Html, Css, Scss, Tailwind.</p>
                    </div>
                </div>
                <div className="skills-main">
                    <h3 className={toggleDark()}>Programming Languages</h3>
                    <div className="skill-sub">
                        <i class={`fa-solid fa-arrow-turn-up ${toggleDark()}`}></i>
                        <p className={toggleDark()}>Javascript, Python, C.</p>
                    </div>
                </div>
                <div className="skills-main">
                    <h3 className={toggleDark()}>Libraries</h3>
                    <div className="skill-sub">
                        <i class={`fa-solid fa-arrow-turn-up ${toggleDark()}`}></i>
                        <p className={toggleDark()}>
                            React, Redux, Jquery, Django, Bootstrap.
                        </p>
                    </div>
                </div>
                <div className="skills-main">
                    <h3 className={toggleDark()}>Operating System</h3>
                    <div className="skill-sub">
                        <i class={`fa-solid fa-arrow-turn-up ${toggleDark()}`}></i>
                        <p className={toggleDark()}>Linux, Windows.</p>
                    </div>
                </div>
                <div className="skills-main">
                    <h3 className={toggleDark()}>Other</h3>
                    <div className="skill-sub">
                        <i class={`fa-solid fa-arrow-turn-up ${toggleDark()}`}></i>
                        <p className={toggleDark()}>Github, Jira.</p>
                    </div>
                </div>
            </div>
            <div className="skills">
                <h2 className={toggleDark()}>Experience</h2>
                <div className="experiences">
                    <a
                        className={toggleDark()}
                        href="https://privateyebd.com"
                        target="blank"
                    >
                        <h3 className={toggleDark()}>Privateye Limited</h3>
                    </a>
                    <p className={toggleDark()}>
                        December, 2020 - continuing as <strong>Fronend Developer</strong>
                    </p>
                </div>
            </div>
            <div className="skills">
                <button className="cv-btn" onClick={onButtonClick}>
                    Click to download my CV
                </button>
            </div>
        </div>
    );
}

export default About;
