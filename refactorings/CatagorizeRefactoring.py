import pandas

def main1():
    pd = pandas.read_csv("/Users/malinda/Documents/Research_Topic_2/RMiner_Maven/generations/refactorings.csv")
    data_frame = pd.groupby("RefactoringType")
    sb=""
    groups = []
    precisions = {}
    for k in data_frame.groups.keys():
        group = data_frame.get_group(k)
        total_count = 0
        total_true= 0
        for x in group["TrueRefactoring"]:
            if x==True:
                total_count+=1
                total_true+=1
            elif (x==False):
                total_count += 1
        precision = "in progress" if total_count==0 else str(round(total_true*100/total_count,2))+"%"
        # precisions.update({k:precision})
        groups.append(group)
        sb = """<!DOCTYPE html>
        
        
<html>
<head>
 <style>
     table, th, td {
         border: 1px solid black;
     }

 </style>
</head>
<body>

<H1>An Empirical Study of Frequent Code Edit Patterns In Machine Learning Systems</H1>
<body><HTML><H2> Refactoring Type : <i>"""+ k +"""</i> : Total - <i>"""+str(group.count()["Project"])+"""</i> : Precision -<i>"""+precision +"""</i></H2>

<table>
 <tr>
  <th>Project</th>
  <th>RefactoringType</th>
  <th>RefactoringLink</th>
  <th>CommitLink</th>
  <th>TrueRefactoring?</th>
  <th>Description</th>
  <th>File</th>
 </tr>
 """
        for index,row in group.iterrows():
            sb=sb+"<tr>"
            sb=sb+"<td>"+row["Project"]+"</td>\n"
            sb = sb + "<td>" + row["RefactoringType"] + "</td>\n"

            sb = sb + "<td><a href=\""+ row["RefactoringLink"]+"\">RefactoringLink</a></td>"
            sb = sb + "<td><a href=\"" + row["CommitLink"] + "\">CommitLink</a></td>"
            if (row["TrueRefactoring"]==True):
                sb = sb + "<td>" + "Yes" + "</td>\n"
            elif (row["TrueRefactoring"]==False):
                sb = sb + "<td>" + "No" + "</td>\n"
            else:
                sb = sb + "<td>" + "" + "</td>\n"
            sb = sb + "<td>" + row["Description"] + "</td>\n"
            sb = sb + "<td>" + row["File"] + "</td>\n"
            sb = sb + "</tr>\n"

        sb = sb+ """</table>

</body>
</html>"""

        result = pandas.concat(groups)
        result.to_csv('/Users/malinda/Documents/Research_Topic_2/RMiner_Maven/generations/refactorings.csv',index=False)
        f = open(k.replace(" ","_")+".html", "w")
        f.write(sb)
        f.close()











if __name__ == '__main__':
  main1()
