# Trkkr
## Milestones and realted tasks
[Brainstorming Notes](https://docs.google.com/document/d/1tGIkbX_Jc_wwIDTFyM7HNC8PPHtoryvsQfFPuvLEh7Y/edit)
- [x] Create google form so spreadsheet can begin populating
  - [google form](https://forms.gle/Lj7ADpVdwV1dVyiw9)
- [ ] Create streamlit form so that app can be contained to one website
- [ ] Find out how to pull data from google spreadsheet
  - [Public](https://docs.streamlit.io/en/stable/tutorial/public_gsheet.html)
  - [Private](https://docs.streamlit.io/en/stable/tutorial/private_gsheet.html)
- [ ] Figure out all types of graphs
  - List all types of graph in this list (y vs x)
  - Body Weight vs Day
  - Reps @ given weight vs Day
  - ORM(calcualted) vs Day
- [ ] For above graphs, create data aggreagation code for (a yet to be determined) standard form 
  - i.e. Column 1 is date, column 2 is calculated ORM, which then the graph function
- [ ] Make graph sexy
- [ ] Design around user workflows
   - i.e. brainstorm how app will be used and make sure its frictionless to use it that way
- [ ] Feature: Implment a goals system, should display %/goal attained after every submission
- [ ] Feature: Implemnt smoothing using a 7 day moving average
- [ ] Feature: Predict actual weight (just introduce a bias to guess their fasting weight)
- [ ] Figure out gains system
- [ ] Monetize gains ( gains = giftcards provided by ad sponsers if we got popular enough)

## Git Commands

`git clone <repo url>`  

`git checkout -b <branch name>`

`git branch <name>`

`git commit -a`
- (open up in vim)
- (press "i" to write text, esc to stop writing text, then `:wq` to save commit msg)
`git branch`
- View which branch you are on
  
`git pull origin main`
  - pulls the current master branch
  
  
`git push origin <branch name>`
  - push your branch
  
  
If ready to merge, create pull request. If its ez, just review it yourself and merge. If not sure, add me as reviewer and text me
