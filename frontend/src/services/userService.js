const API_URL = "http://127.0.0.1:5000";

export async function getUsers(){ // Export makes it available to the other files, async as it allows us to use await
    const response = await fetch(`${API_URL}/users`); // Call users endpoint
    if(!response.ok){
        throw new Error("Failed to fetch users");
    }
    return response.json(); // Convert response to JSON 
}

export async function createUser(username, password){
    const response = await fetch(`${API_URL}/users`, {
        method:"POST",
        headers:{
            "Content-Type": "application/json" // Tell backend we're ending JSON
        },
        body: JSON.stringify({username, password}) // Convert JS object to JSON
    });

    if (!response.ok){
        throw new Error("Failed to create user")
    }
    return response.json() // May return messages from backend for the user
}

export async function deleteUser(id){
    const response = await fetch(`${API_URL}/users/${id}`, {
        method:"DELETE",
    });

    if(!response.ok){
        throw new Error("Failed to delete user")
    }

    return response.json()
}

export async function updateUser(userid, username, password){
    const response = await fetch(`${API_URL}/users/${userid}`, {
        method:"PUT",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({username, password})
    });
    
    if(!response.ok){
        throw new Error("Failed to update user")
    }

    return response.json()
}

