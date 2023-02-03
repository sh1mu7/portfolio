import React, { useContext } from 'react';
import { DarkModeContext } from '../../DarkModeContext';

function Education({certificate, institute, session}) {
    const {darkMode} = useContext(DarkModeContext);
    const darkToggle =()=>{
        return darkMode ? "dark" : "";
    }
  return (
    <div className="education">
          <p className={`institute ${darkToggle()}`}>
            <strong>{certificate}</strong>
          </p>

          <p className={darkToggle()}>{institute}</p>

          <p className={darkToggle()}>{session}</p>
        </div>
  )
}

export default Education