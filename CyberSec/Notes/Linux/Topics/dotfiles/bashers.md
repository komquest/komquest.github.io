```bash
### Source This from main .bashrc or .zshrc!!!
### Make sure you set private variables/secrets in main bashrc or zshrc file!!!

alias h_push="/home/${USER}/Scripts/gitpush.sh ${H_KEY}"                                                                                              
alias h_pull="/home/${USER}/Scripts/gitpull.sh ${H_KEY}"                                                                                              
alias k_push="/home/${USER}/Scripts/gitpush.sh ${K_KEY}"                                                                                              
alias k_pull="/home/${USER}/Scripts/gitpull.sh ${K_KEY}"                                                                                              
alias i='ip -c a sh | grep -E -o "192[.]168[.]122[.][0-9]{1,3}|10[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}"'                                            
alias miniConda_create='conda create python=3.12 -n '                                                                                                 
alias miniConda_list='conda info -e'                                                                                                                  
alias miniConda_activate='conda activate '                                                                                                        
                                                                                                                                                      
### FUNCTIONS                                                                                                                                         
                                                                                                                                                      
# This will take space separated tabs and grep looking for them to cat everything into vim                                                            
# Useful if you need to look up specific commands                                                                                                     
# Note: All files must have a tabs line like "__tabs: linux windows nmap etc"                                                                         
tools_search_tags() {                                                                                                                                  
    if [ $# -eq 0 ]; then                                                                                                                             
        echo "Usage: search_tags <tag1> [tag2] [tag3] ..."                                                                                            
        echo "Example: search_tags smb linux"                                                                                                         
        return 1                                                                                                                                      
    fi                                                                                                                                                
                                                                                                                                                      
    # Build the grep pattern from all arguments                                                                                                       
    local pattern=$(printf "%s|" "$@")                                                                                                                
    pattern=${pattern%|}  # Remove trailing |                                                                                                         
                                                                                                                                                      
    grep -irnE '^__tags' $(pwd) | grep -E "$pattern" | awk -F ':' '{print $1}' | xargs -I {} cat "{}" | vim -                                         
}                                                                                                                                                     
                                                                                                                                                      
tools_nmap_basic_search() {                                                                                                                           
    ports=$(nmap -p- --min-rate=1000 -T4 ${1} | grep '^[0-9]' | awk -F '/' '{print $1}' | tr '\n' ',' | sed s/,$//)                                   
    nmap -p${ports} -sC -sV ${1}                                                                                                                      
}  

```