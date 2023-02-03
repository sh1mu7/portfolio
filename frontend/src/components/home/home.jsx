import React, { useContext } from "react";
import { Link, useParams } from "react-router-dom";
import { DarkModeContext } from "../../DarkModeContext";

function Home() {
  const {bid} = useParams();
  console.log(bid);
  const { darkMode } = useContext(DarkModeContext);
  const toggleDark = () => {
    return darkMode ? "dark" : "";
  };
  return (
    <div className={"home_main " + toggleDark()}>
      <h2>I Am Nittanando Sarkar!</h2>
      <p className={"home-about " + toggleDark()}>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae amet
        porro nisi sunt nam inventore ipsam ducimus quisquam ad nesciunt. Lorem
        ipsum dolor sit amet consectetur adipisicing elit. Dignissimos
        exercitationem voluptates sapiente nam debitis provident tenetur
        assumenda rem voluptate enim. Lorem ipsum dolor sit, amet consectetur
        adipisicing elit. Eos, quidem!
      </p>
      <div className="home-social-media">
        <p className={toggleDark()}>Find me on</p>
        <div className="social-media-icon-wrapper">
          <Link>
            <i className={"s-icon fa-brands fa-github-alt " + toggleDark()}></i>
          </Link>
          <Link>
            <i className={"s-icon fa-brands fa-twitter " + toggleDark()}></i>
          </Link>
          <Link>
            <i
              className={"s-icon fa-brands fa-linkedin-in " + toggleDark()}
            ></i>
          </Link>
          <Link>
            <i className={"s-icon fa-solid fa-envelope " + toggleDark()}></i>
          </Link>
        </div>
      </div>

      <div className="home-post">
        <h3>Posts</h3>
        <div className="post-wrapper">
          <span className="post-single">
            <p className={"date-post " + toggleDark()}>22 march 2022</p>
            <Link to='/blog/1'>
              <p className={toggleDark()}>Revolutionary NFT project Chingari</p>
            </Link>
          </span>
          <span className="post-single">
            <p className={"date-post " + toggleDark()}>03 feb 2022</p>
            <Link>
              <p className={toggleDark()}>Post Title</p>
            </Link>
          </span>
        </div>
      </div>

      <div className="home-project">
        <h3>Projects</h3>
        <div className="post-wrapper">
          <table className={toggleDark()}>
            <tbody>
              <tr>
                <td>
                  <Link to="/projects/1">Tax Management System</Link>
                </td>
                <td>
                A Bootstrap (Frontend) & Django (Backend) based Management 
                System Application for our respected client Roy and Associates 
                to handle large numbers of files and data for 
                their respective clients
                </td>
              </tr>
              <tr>
                <td>
                  <Link to="projects/3">Loan Management System</Link>
                </td>
                <td>
                A Bootstrap (Frontend) & Django (Backend) based Management
                 System Application for our respected client ALO Somobay 
                 Shomiti to run their business
                </td>
              </tr>
              <tr>
                <td>
                  <Link to="projects/2">Blog Application</Link>
                </td>
                <td>
                A Bootstrap (Frontend) & Django (Backend) based 
                Blog Application for our Respected Client Priyanka Biswas
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Home;
