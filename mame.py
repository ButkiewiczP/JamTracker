#/usr/bin/python

##################################
# NOTES
#
#
##################################

MAME_NOT_FOUND_SLEEP_INTERVAL = 10
MAME_WINDOW_NAME = "MAMEOutput"
MAME_WINDOW_NAME_JAM = "MAME: NBA Jam TE (rev 4.0 03/23/94) [nbajamte]"
MAME_MESSAGE_GET_SAVE_STATE = "MAMEOutputGetSaveState"
MAME_MESSAGE_DID_SAVE_STATE = "MAMEOutputDidSaveState"
MAME_MESSAGE_MAME_START = "MAMEOutputStart"
MAME_MESSAGE_MAME_STOP = "MAMEOutputStop"
MAME_MESSAGE_UPDATE_STATE = "MAMEOutputUpdateState"
MAME_MESSAGE_REGISTER_CLIENT = "MAMEOutputRegister"
MAME_MESSAGE_UNREGISTER_CLIENT = "MAMEOutputUnregister"
MAME_MESSAGE_GET_ID_STRING = "MAMEOutputGetIDString"

# window parameters
#define OUTPUT_WINDOW_CLASS         TEXT("MAMEOutput")
#define OUTPUT_WINDOW_NAME          TEXT("MAMEOutput")

# These messages are sent by MAME:

# OM_MAME_START: broadcast when MAME initializes
#      WPARAM = HWND of MAME's output window
#      LPARAM = unused
# define OM_MAME_START               TEXT("MAMEOutputStart")

# OM_MAME_STOP: broadcast when MAME shuts down
#      WPARAM = HWND of MAME's output window
#      LPARAM = unused
#define OM_MAME_STOP                TEXT("MAMEOutputStop")

# OM_MAME_UPDATE_STATE: sent to registered clients when the state
# of an output changes
#      WPARAM = ID of the output
#      LPARAM = new value for the output
#define OM_MAME_UPDATE_STATE        TEXT("MAMEOutputUpdateState")


#
# These messages are sent by external clients to MAME:
#

# OM_MAME_REGISTER_CLIENT: sent to MAME to register a client
#      WPARAM = HWND of client's listener window
#      LPARAM = client-specified ID (must be unique)
#define OM_MAME_REGISTER_CLIENT     TEXT("MAMEOutputRegister")

# OM_MAME_UNREGISTER_CLIENT: sent to MAME to unregister a client
#      WPARAM = HWND of client's listener window
#      LPARAM = client-specified ID (must match registration)
#define OM_MAME_UNREGISTER_CLIENT   TEXT("MAMEOutputUnregister")

# OM_MAME_GET_ID_STRING: requests the string associated with a
# given ID. ID=0 is always the name of the game. Other IDs are
# only discoverable from a OM_MAME_UPDATE_STATE message. The
# result will be sent back as a WM_COPYDATA message with MAME's
# output window as the sender, dwData = the ID of the string,
# and lpData pointing to a NULL-terminated string.
#      WPARAM = HWND of client's listener window
#      LPARAM = ID you wish to know about
#define OM_MAME_GET_ID_STRING       TEXT("MAMEOutputGetIDString")
