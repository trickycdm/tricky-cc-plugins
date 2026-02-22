---
description: Create a copy pasteable summary of the current session designed to allow you to /clear and bootstrap a new session with all the relevant context. 
---

I would like to reset the Claude Code session, but I don't want to have to set all the relevant context on what we just done, and describe whatever is relevant. Collate a detailed overview of all the work carried out, file links and any details that will be useful for the LLM when starting a new session. Once you have this information construct it into a prompt which could full initialize a new session, explaining the context that we have just finished a session and want to pick up where we left off. Output this in a format I can just copy paste into a new session. 

Ensure any temp plans created are written to the .features/<this_feature> directory of the workspace to the next session has full and complete context. 

If there is an existing WORKLOG.md in that directory, make sure it is fully upto date. 

Ensure your final output references both these docs along with your summary context. 

