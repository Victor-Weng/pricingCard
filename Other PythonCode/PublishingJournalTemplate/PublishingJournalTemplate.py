namelist = [



]



journallist = [
    "Econometrica"
    ,"Journal of Economic Perspectives"
    ,"Journal of Consumer Psychology"
    ,"Review of Economic Studies"
    ,"Quantitative Economics"
    ,"Quarterly Journal of Economics"
    ,"The Economic Journal"
    ,"Experimental Economics"
    ,"Journal of Behavioral and Experimental Economics"
    ,"Journal of Behavioral and Experimental Finance"
    ,"Journal of Economic Behavior & Organization"
    ,"Journal of Behavioral Decision Making"
    ,"Journal of Economic Psychology"
    ,"Organizational Behavior and Human Decision Processes"
    ,"Frontiers in Behavioral Economics"
    ,"Journal of Behavioral Finance"
    ,"Games and Economic Behavior"
    ,"International Journal of Applied Behavioral Economics"
    ,"Journal of Consumer Research"
    ,"Journal of Behavioural Economics and Social Systems"
    ,"Journal of Behavioural Economics, Finance, Entrepreneurship, Accounting and Transport"
    ,"Journal of Economics and Behavioral Studies"
    ,"Review of Behavioral Economics"
    ,"Health Psychology"
]
emaillist = ["a", "b", "c", "d"]
texttemplate = ""

for i in range(len(namelist)):
    g = int(i)
    name = namelist[g]
    journal = journallist[g]
    email = emaillist[g]
    texttemplate = f"Dear {name},\n\nI’m writing to inquire about the suitability of my paper, “Evaluating Beyond Meat’s Success in the Consumer Market for Plant-Based Meat” for {journal}.\n\nThe paper explores the application of behavioral economics in changing consumer behavior and perceptions of plant-based meats, a significant step in reducing the issue of climate change. The presented research highlights both the effectiveness and unexplored potential of behavioral economics in initiating wide-scale change—which would be insightful for your readers. I hope you will consider evaluating the files to see if it falls within {journal}'s scope. The title and abstract are copied below; if you or another editor wishes to read further, I would be happy to send the entirety of the paper.\nI believe that the results would be of great interest and aligns with the journal’s aim of publishing innovative works in economics. If you have any questions, please let me know.\n\nThank you for your time, I’m looking forward to your reply.\n\nBest regards,\n\nVictor Weng"
    print(email + "\n\n" + texttemplate + "\n\n\n")