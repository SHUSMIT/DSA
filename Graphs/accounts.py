class DisjointSetUnion:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]
    
    def findUparent(self,node):
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.findUparent(self.parent[node])
        
        return self.parent[node]
    
    def union(self,x,y):
        up_x = self.findUparent(x)
        up_y = self.findUparent(y)

        if up_x == up_y:
            return
        
        elif self.size[up_x] > self.size[up_y]:
            self.parent[up_y] = up_x
            self.size[up_x] += self.size[up_y]
        else:
            self.parent[up_x] = up_y
            self.size[up_y] += self.size[up_x]


def accounts_merge(accounts):
    ## array of array of accounts/email
    email_id_dict = {}
    email_to_name = {}

    idx = 0
    ## give each email a unique id/node
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            if email not in email_to_id: ## unique only
                email_to_id[email] = idx ## mail : idx
                email_to_name[email] = name ## mail : name for reconstruct
                idx += 1

    
    # union mails in same account to the first:  first -> (second, third ... ) all connected
    for account in accounts:
        first_mail = account[0]
        for mail in account[1:]:
            ds.union(email_id_dict[first_mail],email_id_dict[mail])
    
    ## marge all to ultimate parent
    ## dict of parent_idx = [emails] 
    parent_email = {}
    for email,idx in email_id_dict.items():
        up_email = findUparent(idx) ## find ultimate parent of that email id, of that idx ( all coonected by dsu above )

        if up_email not in parent_email:
            parent_email[up_email]= [] ## index array

        parent_email[up_email].append(email)
    
    ## reconstruct

    for email in email_to_name:
        name = email_to_name[emails[0]]
        result.append([name] + sorted(emails))

    return result

'''
DSU Initialization:
Create the DSU after all emails have been assigned IDs.

Union by Email IDs:
For each account, union all emails to the first email in the account.

Grouping:
Use DSU to find the ultimate parent of each email and group emails by their parent.

Reconstruction:
For each group, use the name associated with any email in the group (they all belong to the same person), and sort the emails.

'''