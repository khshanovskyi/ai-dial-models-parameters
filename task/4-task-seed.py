from task.app.main import run

# TODO:
#  Try the `seed` parameter:
#       It allows us to reduce entropy by making the model's output more deterministic.
#       There's no universally "best" seed - any integer works fine. Common approaches:
#            - For testing: Use simple values like 42, 123, or 1000
#       Default: None or random unless specified on the LLM side
#  User massage: Name a random animal

run(
    deployment_name="gpt-4o",
    print_request=True, # Switch to False if you do not want to see the request in console
    print_only_content=False, # Switch to True if you want to see only content from response
    n=5,  # Number of chat completion choices to generate for each input message,
    temperature=1.0, # Adjust the temperature parameter here
    seed=123, # Use seed parameter to make output more deterministic
)

# Check the content in choices. The expected result is that in almost all choices the result will be the same.
# If you restart the app and retry, it should be mostly the same.
# Also, try it without `seed` parameter.
# For Anthropic and Gemini this parameter will be ignored