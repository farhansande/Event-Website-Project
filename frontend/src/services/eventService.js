const API_URL = "http://127.0.0.1:5000";

export async function getEvents(){
    const response = await fetch(`${API_URL}/events`);

    if(!response.ok){
        throw new Error("Failed to fetch events");
    }

    return response.json();
}

export async function createEvent(name, time, location){
    const response = await fetch(`${API_URL}/events`, {
        method:"POST",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify({name, time, location})
    });

    if (!response.ok){
        throw new Error("Failed to create Event")
    }
    return response.json()
}

export async function deleteEvent(id){
    const response = await fetch(`${API_URL}/events/${id}`, {
        method:"DELETE",
    });

    if(!response.ok){
        throw new Error("Failed to delete Event")
    }

    return response.json()
}

export async function updateEvent(id, name, time, location){
    const response = await fetch(`${API_URL}/events/${id}`,{
        method:"PUT",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify({name, time, location})

    });

    if(!response.ok){
        throw new Error("Failed to update Event")
    }

    return response.json()
}