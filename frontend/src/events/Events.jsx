import useSWR from "swr"; // Without curly braces = whatever name we give it eg useSWR doesn't matter when importing, as the file exports one main thing
import { fetcher } from "../services/fetcher"; // importing specific functions
import { API_URL } from "../services/config";
import { createEvent, deleteEvent, updateEvent } from "../services/eventService";
import { useState } from "react";

// Parent controller

export default function Events(){ // Default function means, if no argument is given, it will return default

    const {data, error, isLoading, mutate} = useSWR( // Replaces loadEvents, use mutate after adding/deleting events
        `${API_URL}/events`,
        fetcher
    )

    const[newEvent, setNewEvent] = useState({ // newEvent stores the object name, etc. While setNewEvent is the function to update setNewEvent
        EventName: "",
        EventTime: "",
        EventLocation: "",
        EventDescription: ""
    });

    // Handlers

    const handleCreate = async ()  => {
        if(!newEvent.EventName) return alert("Event name is required");
        await createEvent(newEvent);
        mutate(); // Refresh the events
        setNewEvent({EventName: "", EventTime: "", EventLocation: "", EventDescription: ""});
    };

    if(isLoading) return <p> Loading events... </p>;
    if(error) return <p> Failed to load events </p>;

    return( // Tells react what to render on the page
        <div>
            <h1 style={{ textAlign: 'center' }}>Events</h1>
            {data.length === 0 ? (
                <p> No events found. </p>
            ) : (
               <ul>
                {data.map(event =>(
                    <li key = {event.EventID}>
                        <p>{event.EventName} - {event.EventTime} at {event.EventLocation} {}</p>
                        {event.EventDescription}
                    </li>
                ))}
               </ul> 
            )}

            <div style={{ marginBottom: "20px", textAlign: "center" }}>
                <input
                    type = "text"
                    placeholder = "Event Name"
                    value = {newEvent.EventName}
                    onChange={(e) => setNewEvent({...newEvent, EventName: e.target.value})} // e stands for object (can be called anything doesn't have to be e), ...newEvent to copy everything prev.
                />

                <input
                    type = "text"
                    placeholder = "Event Time"
                    value = {newEvent.EventTime}
                    onChange={(e) => setNewEvent({...newEvent, EventTime: e.target.value})}
                />
    
            </div>
        </div>
    );
} 