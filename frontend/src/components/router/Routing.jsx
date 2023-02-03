import React from 'react';
import { Route, Routes } from "react-router-dom";
import About from "../about/about";
import Blog from "../blog/blog";
import BlogPostSingle from '../blog/blogPostSingle';
import Home from "../home/home";
import Project from "../projects/Project";
import ProjectSingle from '../projects/ProjectSingle';


function Routing() {
  return (
    <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/blog" element={<Blog />} />
        <Route path="/projects" element={<Project />} />
        
        <Route path="/projects/:id" element={<ProjectSingle/>}/>
        <Route path="/blog/:bid" element={<BlogPostSingle/>}/>
    </Routes>
  )
}

export default Routing



        // <Route path="/projects/tax-management-system" element={<ProjectSingle />} />
        // <Route path="/projects/priyankar-rafkhata" element={<ProjectSingle />} />

        // {
        //   ProjectData.map((index, item) => {
        //     return (<Route path={item.url} element={<ProjectSingle key={index} index={index} item={item}  />} />);
        //   })
        // }

        // <Route path="/projects/project-details/:id" render={props =>(
        //   <ProjectSingle {...props}/>
        // )} />