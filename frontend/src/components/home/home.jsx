import React, {useContext, useEffect, useState} from "react";
import {Link, useParams} from "react-router-dom";
import {DarkModeContext} from "../../DarkModeContext";
import axios from "axios";

function Home() {
    const {bid} = useParams();
    console.log(bid);
    const {darkMode} = useContext(DarkModeContext);
    const toggleDark = () => {
        return darkMode ? "dark" : "";
    };
    const [data, setData] = useState([]);
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/user/website/").then((response) => {
            console.log(response.data)
            setData(response.data);
        }, (error) => {
            console.log(error.data);
        })
    }, []);
    return (
        <div className={"home_main " + toggleDark()}>

            {data.length > 0 && (<>
                <h2>I am {data[0].author}!</h2>
                <p className={"home-about " + toggleDark()}>
                    {data[0].objectives}

                </p>
                <div className="home-social-media">
                    <p className={toggleDark()}>Find me on</p>

                    <div className="social-media-icon-wrapper">
                        <a href={data[0].github_link} target="_blank" rel="noreferrer noopener">
                            <i className={"s-icon fa-brands fa-github-alt " + toggleDark()}></i>
                        </a>


                        <a href={data[0].linkedin_link} target="_blank" rel="noreferrer noopener">
                            <i
                                className={"s-icon fa-brands fa-linkedin-in " + toggleDark()}
                            ></i>
                        </a>
                        <a href={"mailto:" + data[0].email}>
                            <i className={"s-icon fa-solid fa-envelope " + toggleDark()}></i>
                        </a>

                    </div>
                </div>
            </>)}


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
