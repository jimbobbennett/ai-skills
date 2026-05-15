---
title: 'Build A Terrible API For People You Hate (Mar 2024 draft)'
conference: 'unknown (deck source only)'
year: 2024
source: 'Apple Keynote deck'
source_file: '~/Desktop/build-an-api-for-people-you-hate 3.key'
deck_mtime: '2024-03-12'
version: 'v1 (earliest preserved draft, 36 slides, 7 steps)'
paired_transcripts:
  - 2024-apidays-ny-zAOaynEQGbs.md
  - 2024-nordicapis-austin-1-h6JUdMrraCk.md
pairing_note: 'Same Terrible API talk as the apidays NY and Nordic APIs Austin transcripts. This is the earliest preserved draft on disk.'
---

_Source: Apple Keynote deck. No video / no timestamps. Structured by slide number. Each slide section captures the on-slide text (title + body) and Jim's presenter notes — the notes are the spoken narration._

## Slide 1 — Build A Terrible API For People You Hate

**Body:**
Jim Bennett

Principal developer advocate
liblab

**Notes:**
VS Code
Llama store demos in container
Llama store DB reset
Llama store running
Docs in a browser
Login to liblab
## Slide 2 — Who has worked with someone they hated?

**Body:**
Is it time for malicious compliance?
## Slide 3 — You’ve been asked to create an API for someone you hate…

**Body:**
Is it time for malicious compliance?
## Slide 4 — We need an API for a ticketing system

**Body:**
But we hate the person we need to build it for…
## Slide 5 — We could be nice,

**Body:**
Let’s build a terrible API!
## Slide 6 — Hi, I’m Jim

**Body:**
He/Him

Principal developer advocate
liblab

@jimbobbennett
linktr.ee/jimbobbennett

**Notes:**
I’m Jim
Describe
You can find me on social at JimBobBennett - connect and say hello
## Slide 7 — 7 steps to build a terrible API for people you hate

**Body:**
The best docs are…
## Slide 8 — Step 1

**Body:**
The best API docs are…
## Slide 9 — Nice Jim would…

**Body:**
provide an OpenAPI spec!

Industry standard and can be used to generate decent documentation and client SDKs.
## Slide 10 — Step 2

**Body:**
GET all the things!
## Slide 11 — How do we create a new user?

**Body:**
We GET a new user obviously!
## Slide 12 — HTTP request methods

**Body:**
GET
POST
PUT
PATCH
DELETE
## Slide 13 — Nice Jim would…

**Body:**
support request methods correctly, using POST to create a new user.
## Slide 14 — Step 3

**Body:**
Naming things is hard so let’s not bother doing it well.
## Slide 15 — We need lots of ticket endpoints

**Body:**
/add_ticket - add a ticket
/update_ticket - update a ticket
/all_tickets - get all tickets
/tikcet - get one ticket. Was spelled wrong, so we can’t change it now!
## Slide 16 — Nice Jim would…

**Body:**
support request methods correctly, so we can have just one endpoint:

/ticket
/ticket/{id}
## Slide 17 — Step 4

**Body:**
Request bodies are better than path or query parameters.
## Slide 18 — To get a ticket, put the ID in the request body

**Body:**
Make a request to /tikcet
Pass the ticket ID in the body:
{
  “ticket_id”: 1
}
## Slide 19 — To update a ticket, put the ID in the request body

**Body:**
Make a request to /update_ticket
Pass the ticket ID in the body with the rest of the fields to update:
{
  “ticket_id”: 1
  “status”: “done”
}
## Slide 20 — To search for a ticket, put the search criteria in the request body

**Body:**
Make a request to /search_tickets
Pass the search criteria in the body:
{
  “status”: “open”
}
## Slide 21 — Nice Jim would…

**Body:**
use path parameters and query parameters instead of sending identifiers in a request body
## Slide 22 — Step 5

**Body:**
Non-200 status codes are bad and make client code throw exceptions!

Always return 200!
## Slide 23 — Return 200, and put the error in the response!

**Body:**
Status: 200 OK

{
  “status”: 404,
  “message”: “Ticket not found”
}
## Slide 24 — HTTP status codes mean things

**Body:**
1xx - hold please
2xx - here you go!
3xx - go away
4xx - you mucked up
5xx - I mucked up
## Slide 25 — HTTP status codes mean things

**Body:**
200 - OK!
400 - bad request
401 - unauthorized
404 - not found
418 - I’m a teapot
## Slide 26 — Nice Jim would…

**Body:**
return the appropriate status code for an error, and include more details in an error response body.
## Slide 27 — Step 6

**Body:**
Atomic updates? Nah!
## Slide 28 — Creating a user will insert into 2 tables

**Body:**
2 tables - user and user_details
Record inserted into user table
Data is missing from the request, so an insert into the user_details table fails
API returns an error
## Slide 29 — Creating a user will insert into 2 tables

**Body:**
User retries - duplicate in the user table
## Slide 30 — Nice Jim would…

**Body:**
ensure all updates are atomic - if the API call fails the system is in the same state as before the call.
## Slide 31 — Step 7

**Body:**
We know better than those ‘consistent data types’ folks!
## Slide 32 — Return different data types depending on the endpoint

**Body:**
When getting all tickets, return IDs as comma separated values
When getting one ticket, return the ticket as JSON
When getting a user, return the user as XML!
## Slide 33 — Pass strings instead of numbers

**Body:**
The salary field on the user is a string, so we can handle different currencies!
## Slide 34 — Nice Jim would…

**Body:**
have consistency with responses, returning everything as JSON, as well as using the right data type for each field.
## Slide 35 — What if we don’t hate them?

**Body:**
Provide an OpenAPI spec
Use correct request methods
Have good naming
Use path parameters
Return proper status codes
Always do atomic updates
Use consistent data types
## Slide 36 — Hi, I’m Jim

**Body:**
He/Him

Principal developer advocate
liblab

@jimbobbennett
linktr.ee/jimbobbennett

**Notes:**
I’m Jim
Describe
You can find me on social at JimBobBennett - connect and say hello
