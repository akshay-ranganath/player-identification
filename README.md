# Player Identification

## Objective

The purppose of the project is to identify the player in an image. When multiple players are shown, we should be able to identify at least the primary person shown in the image.

## Workflow

1. Take an image
2. Pass it to a vision-based LLM to identify 2 things:
    * Team name
    * Player number from the T-Shirt
3. Once the team and T-Shirt number are identified, use the information to identify the player.


### Player Indentification

To identify a player, we want to support a flexible mechanism. The player information can be in one of the places:

* CSV file
* Database
* Webpage that contains the player information

This information will be passed into the LLM as a tool. The tool supplied will be configurable and part of the `.env` file.


## Troubleshooting

If you run into issues, make sure to run the following.

```
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN
unset AWS_PROFILE  # optional, we'll explicitly pass it anyway
```

This will ensure other AWS picks up the right 

sample url: https://res.cloudinary.com/dbmataac4/image/upload/v1765486287/ghgewenoaznomnmsutrv.jpg