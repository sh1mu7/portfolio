import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { DarkModeContext } from "../../DarkModeContext";
import { BLogData } from "../data/blogData";
import BlogPost from "./blog-post-template";
import Tags from "./tags-blog";

function Blog() {
  const { darkMode } = useContext(DarkModeContext);
  return (
    <div className="blog_main">
      <h2 className={darkMode ? "dark" : ""}>Posts</h2>
      <div className="blog-secondary-wrapper">
        <div className="blog-list-wrapper">
          {BLogData.map((post, index) => {
            return <BlogPost post={post} key={index} />;
          })}
        </div>
        <div className="tags-wrapper">
          <h3 className={`tag ${darkMode ? "dark" : ""}`}>Tags</h3>
          <div className="tags-container">
            <Tags />
            <Tags />
            <Tags />
            <Tags />
            <Tags />
          </div>
          <Link className={`view-all ${darkMode ? "dark" : ""}`}>
            View all <i className="fa-solid fa-arrow-right-long"></i>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default Blog;
