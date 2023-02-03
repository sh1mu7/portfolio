import React, { useContext } from "react";
import { useLocation, useParams } from "react-router-dom";
import {
  EmailShareButton,
  FacebookShareButton,
  LineShareButton,
  TwitterShareButton,
  WhatsappShareButton,
} from "react-share";
import { DarkModeContext } from "../../DarkModeContext";
import { BLogData } from "../data/blogData";

function BlogPostSingle() {
  const { bid } = useParams();
  const blog = BLogData.find((i) => (i.bid = bid));

  const location = useLocation();
  const shareUrl = "http://192.168.0.129:3000" + location.pathname;

  const { darkMode } = useContext(DarkModeContext);
  const darkModeToggle = () => {
    return darkMode ? "dark" : "";
  };
  return (
    <div className="project-single-main">
      <div className="project-single-wrapper">
        <h1 className={darkModeToggle()}>{blog.title}</h1>
        <img src={blog.image} alt="blog" />
        <p className={darkModeToggle()}>Posted on {blog.date}</p>

        <hr />
        <p className={`blog-content-txt ${darkModeToggle()}`}>
          {blog.description}
        </p>
        <div className={`blog-comment-share ${darkModeToggle()}`}>
          <span>Comments</span>
          <span className="social-media">
            <FacebookShareButton url={shareUrl}>
              <i className="fa-brands fa-facebook-f"></i>
            </FacebookShareButton>
            <EmailShareButton url={shareUrl}>
              <i className="fa-solid fa-envelope"></i>
            </EmailShareButton>
            <LineShareButton url={shareUrl}>
              <i className="fa-brands fa-linkedin-in"></i>
            </LineShareButton>
            <TwitterShareButton url={shareUrl}>
              <i className="fa-brands fa-twitter"></i>
            </TwitterShareButton>
            <WhatsappShareButton url={shareUrl}>
              <i className="fa-brands fa-whatsapp"></i>
            </WhatsappShareButton>
          </span>
        </div>
        <hr />
        <div>
          <div
            className={`comment-list ${darkMode ? "comment-list-light" : ""}`}
          >
            <div className="comment-header">
              <h3 className={darkModeToggle()}>Mahmudul Hasan</h3>
              <p className={darkModeToggle()}>22 April, 2022</p>
            </div>
            <p className={darkModeToggle()}>
              Nice writing Lorem ipsum dolor sit amet consectetur adipisicing
              elit. Esse, minima!
            </p>
          </div>
          <div
            className={`comment-list ${darkMode ? "comment-list-light" : ""}`}
          >
            <div className="comment-header">
              <h3 className={darkModeToggle()}>Mahmudul Hasan</h3>
              <p className={darkModeToggle()}>22 April, 2022</p>
            </div>
            <p className={darkModeToggle()}>
              Nice writing Lorem ipsum dolor sit amet consectetur adipisicing
              elit. Esse, minima!
            </p>
          </div>
        </div>
        <hr />
        <div className="post-comment">
          <h3 className={darkModeToggle()}>Post Your Comment</h3>
          <div className="form-wrapper">
            <form className={darkModeToggle()} action="">
              <label htmlFor="">Name</label>
              <input type="text" placeholder="your name" />
              <label htmlFor="">Email</label>
              <input type="text" placeholder="your mail" />
              <label htmlFor="">Comment</label>
              <textarea placeholder="your comment"></textarea>
              <button>Post</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default BlogPostSingle;
