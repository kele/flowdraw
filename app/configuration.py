from app.configuration_impl import *

# "Bob.*" : "Bob" ## Actors matching 'Bob.*' would be simplified to 'Bob'
actor_mapping = { \
} 

# Ignored actors regexps
ignored_actors = { \
}

# Ignored message labels regexps
ignored_messages = { \
}


configuration = Configuration()
configuration.actor_mapping = actor_mapping
configuration.ignored_actors = ignored_actors
configuration.ignored_messages = ignored_messages
