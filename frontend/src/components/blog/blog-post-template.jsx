import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { DarkModeContext } from "../../DarkModeContext";

function BlogPost({post}) {
  const { darkMode } = useContext(DarkModeContext);
  const toggleDark = () => {
    return darkMode ? "dark" : "";
  };
  return (
    <div className="bp-template_main">
      <div className="img-wrapper">
        <img className="post-img" src={post.image} alt="posts" />
      </div>
      <div className="content-wrapper">
        <h3 className="post-title">
          <Link className={"post-title-link " + toggleDark()} to={`/blog/${post.bid}`}>{post.title}</Link>
        </h3>
        <p className={"post-content " + toggleDark()}>
          {post.description.length > 50 ? `${post.description.substring(0, 50)}...` : post.description}
        </p>
        <span className={"post-date " + toggleDark()}>
          Published on,<i>{post.date}</i>
        </span>
      </div>
    </div>
  );
}

export default BlogPost;
