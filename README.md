# Web Forum

## Student Information

- Name: Jigar Chhatrala
- Stevens Login: jchhatra@stevens.edu

- Name: Akhil Vandanapu
- Stevens Login: avandana@stevens.edu

## Project Information

- Public GitHub Repo URL: https://github.com/jigargc/project3.git
- Estimated Hours Spent: 20+ hours

## Testing

We thoroughly tested using postman and newman to test our code. We also tested our code manually to verify the
correctness of the output.

## Known Bugs and Issues

N/A

## Resolving a Difficult Issue

N/A

## Implemented Extensions

1. **Extension 1: Users and user keys**
    - We implemented users and user keys to allow users to create their own posts.
    - To create new user, use "POST /user" with body {"username": "string", "name":"string"}
    - Both username and name are required fields.
    - If username is not unique, the application will return 400 error.
    - This extension is modified create post to allow users to create their own posts.
    - To delete post key is required.

2. **Extension 2: User profiles**
    - We implemented user profiles to allow users to view and edit.
    - To view user profile, use "GET /user/{{user_id}}"
    - To edit user profile, use "PUT /user/{{user_id}}" with body {"username": "string", "name":"string"}
    - This extension is combine with extension 1 which is crete user.
    - Both username and name are required fields.
    - If user is not found, the application will return 404 error.

3. **Extension 3: Date- and time-based range queries**
    - We implemented date- and time-based range queries to allow users to view posts in a specific date and time range.
    - To view posts in a specific time range, use "GET /posts/dateRange/?start={{start}}&end={{end}}"
    - If start date and end date are not provided, the application will return all posts.
   
4. **Extension 4: User-based range queries** 
    - We implemented user-based range queries to allow users to view posts by a specific user.
    - To view posts by a specific user, use "GET /user/posts/{{user_id}}"
    - If user is not found, the application will return 404 error.

5. **Extension 5: Fulltext search** 
    - We implemented fulltext search to allow users to search posts by msg.
    - To search posts by title and body, use "GET /posts/fullTextSearch/?text={{query}}"
    - If query is not provided, the application will return all posts.
