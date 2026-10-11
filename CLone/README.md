# Clone Porject to local
git clone git@github.com:Ltekuh/cybersecurity-analyst-portfolio.git

# Go into the extracted portfolio folder
cd "$HOME\Downloads\cybersecurity-analyst-portfolio"

# Initialize Git
git init
git branch -M main

# Stage the portfolio files
git add .

# Save the first version
git commit -m "Add cybersecurity portfolio starter"

# Connect your GitHub repository
git remote add origin https://git@github.com:Ltekuh/cybersecurity-analyst-portfolio.git

# Upload the files
git push -u origin main