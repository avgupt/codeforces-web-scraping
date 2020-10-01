import requests
from lxml import html
# see start and end pages and specify in range

def returnAcceptedSubmissions(Username):

    for foo in range(1,2):
        # change address below accordingly
        page = requests.get('https://codeforces.com/submissions/' + Username + '/page/'+ str(foo))
        tree = html.fromstring(page.text)
    
        res = []
    
        verdict = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[6]/span/@submissionverdict')
        contestID = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[4]/a/@href')
        problemID = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[1]/a/text()')

        for i in range(len(contestID)):
            r = list(map(str,contestID[i].split("/")))
            #print(r)
            contestID[i] = r[2]

        for i in range(len(contestID)):
            res.append([contestID[i],verdict[i], problemID[i]])

    
        for i in range(len(res)):
            # change verdict or dont specify at all
            if res[i][1] == "OK":
                solutionPage = requests.get('https://codeforces.com/contest/'+ res[i][0]+'/submission/'+ res[i][2])
                tree2 = html.fromstring(solutionPage.text)
                code = tree2.xpath('.//div[@id="pageContent"]/div[@class="roundbox SubmissionDetailsFrameRoundBox-94336587"]/pre[@id="program-source-text"]//text()')
            
                lines = code[0].split("\r\n")
            
                for i in lines:
                    print(i)
            

