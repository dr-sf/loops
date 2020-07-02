import sys

if len(sys.argv) < 2:
    print("File not found")
    sys.exit()

file = sys.argv[1]
f = open(file)

# max depth of headlines = 5
chapter = [ 0, 0, 0, 0, 0 ]
lines = []


for i in f:
    if i.startswith("#"):
        # split headline
        splits = i.split(" ")
        # check for numbers in headline text
        if len(splits) > 2:
            for char in splits[1]:
                if(char.isdigit()):
                    # remove number
                    i = i.replace(splits[1] + " ", "")
                    break;
        depth = i.count("#") - 1
        number = ""
        # for each headline after ##
        if depth > 0:
            number = " "
            chapter[depth-1] += 1
            for x in range(5-depth):
                chapter[4-x] = 0
        
        # put number together
        for j in range(depth):
            number += str(chapter[j])
            if (j != depth-1):
                number += "."
        
        # put output together
        output = i[:depth + 1] + number + i[depth + 1:]
        lines.append(i.replace(i, output))
    else:
        lines.append(str(i))
f.close()

# delete content
f = open(file,"w")

# write new content
for i in lines:
    f.write(i)