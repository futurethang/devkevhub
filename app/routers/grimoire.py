from fastapi import APIRouter
from fastapi import HTTPException
from app.ai_services.completion import create_completion
from app.models import InitialData
from app.session import session

router = APIRouter()

@router.get("/grimoire/")
async def grimoire_welcome():
    # Get the existing completions from the session data
    test_strings = session.get_data("test_string")
    
    # If there are no existing completions, initialize it as an empty list
    if test_strings is None:
        test_strings = []
    
    # Append the new completion to the list of existing completions
    test_strings.append("Another One!")
    
    # Update the session data with the new list of completions
    session.update_data("test_string", test_strings)
    print('test_strings', session.get_data("test_string"))
    return "Grimoire of the Gardening Arts!"


@router.get("/grimoire/test")
async def get_completion():
    completion = create_completion("you are a Gardening expert", "what is best to plant in Seattle in February?")
    
    # Get the existing completions from the session data
    existing_completions = session.get_data("completion")
    
    # If there are no existing completions, initialize it as an empty list
    if existing_completions is None:
        existing_completions = []
    
    # Append the new completion to the list of existing completions
    existing_completions.append(completion)
    
    # Update the session data with the new list of completions
    session.update_data("completion", existing_completions)
    
    print('completions', session.get_data("completion"))
    return {"completion": existing_completions}


@router.post("/grimoire/new_garden")
async def new_garden(item: InitialData):
    if not item.plant or not item.zipcode or not item.start:
        print('provided input: ', item)
        raise HTTPException(status_code=400, detail="Invalid input")
    return {"plant": item.plant, "zipcode": item.zipcode, "comments": item.comments}

# Idea behind this will be to step through a clietn config, setting the zip and time
# LLM responds with a structured response of plants you could grow in that area
# Back anf forth helps user build a custom tailored garden plan
# Client can handle errors by alerting the backend to a data it cannot parse into UI,
# and LLM can respond with another attempt at the correct structured response. 