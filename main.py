import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Dict

app = FastAPI()

# Define a dictionary to store the sortmaps
sortmaps = {}


# Define endpoints for the API

# Endpoint to retrieve a specific sortmap by ID or all sortmaps if no ID is provided
@app.get("/api/sortmaps")
async def get_sortmaps(id: int = None):
    if id:
        # Return the sortmap with the given ID if it exists
        if id in sortmaps:
            return JSONResponse(content=sortmaps[id])
        # Return an error message if the sortmap with the given ID doesn't exist
        else:
            return JSONResponse(status_code=404, content={"message": "Sortmap not found"})
    # Return a list of all the sortmaps if no ID is provided
    else:
        return JSONResponse(content=list(sortmaps.values()))


# Endpoint to create a new sortmap
@app.post("/api/sortmap")
async def create_sortmap(sortmap: Dict[str, str]):
    # Check for duplicate characters in the sortmap
    if len(sortmap["value"]) != len(set(sortmap["value"])):
        return JSONResponse(status_code=400, content={"message": "Duplicate characters in sortmap"})
    # Add the new sortmap to the dictionary
    sortmap_id = len(sortmaps) + 1
    sortmaps[sortmap_id] = {"id": sortmap_id, "value": sortmap["value"]}
    return JSONResponse(status_code=201, content=sortmaps[sortmap_id])


# Endpoint to update an existing sortmap
@app.put("/api/sortmap/{id}")
async def update_sortmap(id: int, sortmap: Dict[str, str]):
    # Check for duplicate characters in the sortmap
    if len(sortmap["value"]) != len(set(sortmap["value"])):
        return JSONResponse(status_code=400, content={"message": "Duplicate characters in sortmap"})
    # Update the sortmap with the given ID if it exists
    if id in sortmaps:
        sortmaps[id]["value"] = sortmap["value"]
        return JSONResponse(content=sortmaps[id])
    # Return an error message if the sortmap with the given ID doesn't exist
    else:
        return JSONResponse(status_code=404, content={"message": "Sortmap not found"})


# Endpoint to delete an existing sortmap
@app.delete("/api/sortmap/{sortmap_id}")
async def delete_sortmap(sortmap_id: int):
    # Delete the sortmap with the given ID if it exists
    if sortmap_id in sortmaps:
        del sortmaps[sortmap_id]
        return JSONResponse(status_code=204, content={})
    # Return an error message if the sortmap with the given ID doesn't exist
    else:
        return JSONResponse(status_code=404, content={"message": "Sortmap not found"})


# Endpoint to sort text using a specified sortmap
@app.post("/api/order")
async def sort_text(sortmap_id: int, request_data: Dict[str, str]):
    # Check if the sortmap with the given ID exists
    if sortmap_id in sortmaps:
        start_time = time.time()
        sortmap = sortmaps[sortmap_id]["value"]
        text = request_data["request"]
        # Check if all characters in the text are valid for the sortmap
        if all(c in sortmap for c in text):
            # Sort the text according to the sortmap and measure the end time
            sorted_text = "".join(sorted(text, key=lambda c: sortmap.index(c)))
            end_time = time.time()
            # Return the sorted text with additional information about the processing time
            return JSONResponse(content={"sortmap_id": sortmap_id, "response": sorted_text,
                                         "time": int((end_time - start_time) * 1000)})
        else:
            # Return an error message if the text contains invalid characters for the sortmap
            return JSONResponse(status_code=400, content={"message": "Invalid characters in text"})
    else:
        # Return an error message if the sortmap_id is not found in the sortmaps dictionary
        return JSONResponse(status_code=404, content={"message": "Sortmap not found"})
