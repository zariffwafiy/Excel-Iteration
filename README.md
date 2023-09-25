# Excel-Iteration
Iterating through Excel for IVA use case

pseudocode:------------
for each rows, access the column TMLID.
for each value of TMLID, tokenize the value using space as delimeter, will result in n amount of tokens_tmlid.
if there are more than 1 token, duplicate the whole row except for TMLID.
the rest of TMLID from row 1 should be moved to the duplicated row.
repeat duplicating rows with different TMLID until exhaust the tokens_tmlid. the total amount of rows is n.
