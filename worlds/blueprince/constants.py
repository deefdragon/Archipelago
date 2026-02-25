######################
# ITEM KEY CONSTANTS #
######################

# Defines the key for setting the data in a room's info-dict. Used specifically to define what item classification a room is.
ROOM_ITEM_CLASSIFICATION_KEY = "item_classification"
# Defines the key for setting the data in a room's info-dict. Used specifically to define what ID the room is as an item.
ROOM_ITEM_ID_KEY = "item_id"
# Defines the key for setting the data in a room's info-dict. Used specifically to define the key for the array of where the room can be selected.
ROOM_PICK_POSITIONS_KEY = "room_picker_positions"
# Defines the key for setting the data in a room's info-dict. Used specifically to define how many spots the room can place an item like a shovel.
ROOM_ITEM_SPOT_COUNT_KEY = "item_spot_count"
# Defines the key for setting the data in a room's info-dict. Used specifically to define how many chest spots the room can have.
ROOM_CHEST_SPOT_COUNT_KEY = "chest_spot_count"
# defines the key for setting the data in a room's info-dict. Used specifically to define which chess piece is in a room
ROOM_CHESS_PIECE_KEY = "chess_piece"
# Defines the key for setting the data in a room's info-dict. Used specifically to define the general shape of the room for path calculations.
ROOM_LAYOUT_TYPE_KEY = "room_layout"
# room location type key is a key used to set if a room is from the outer rooms
OUTER_ROOM_KEY = "is_outer_room"

INNER_ROOM_KEY = "is_inner_room"
LOCATION_COUNT_KEY = "location_count"


##################
# ITEM CONSTANTS #
##################

# One of the room layout types. Specifically, for dead-end rooms
ROOM_LAYOUT_TYPE_D = "room_layout_type_d"
# One of the room layout types. Specifically, for rooms with 3 entrances
ROOM_LAYOUT_TYPE_T = "room_layout_type_t"
# One of the room layout types. Specifically, for rooms with 2 entrances inline
ROOM_LAYOUT_TYPE_I = "room_layout_type_i"
# One of the room layout types. Specifically, for rooms with 2 entrances NOT inline
ROOM_LAYOUT_TYPE_J = "room_layout_type_j"
# One of the room layout types. Specifically, for rooms with 4 entrances.
ROOM_LAYOUT_TYPE_X = "room_layout_type_x"


# Chess piece values for the room having each of the different chess pieces.
CHESS_PIECE_ROOK = "Rook"
CHESS_PIECE_QUEEN = "Queen"
CHESS_PIECE_KING = "King"
CHESS_PIECE_KNIGHT = "Knight"
CHESS_PIECE_BISHOP = "Bishop"
CHESS_PIECE_PAWN = "Pawn"
CHESS_PIECE_NONE = ""


######################
# ITEM KEY CONSTANTS #
######################

# This corresponds to the index of the item in the item list in the game itself.
ITEM_ELEMENT_INDEX_KEY = "item_element_index"
# Key of the item ID in the item data table.
ITEM_ID_KEY = "item_id"
# Key of the item's classification in the item data table.
ITEM_ITEM_CLASSIFICATION_KEY = "item_classification"


##################
# ITEM CONSTANTS #
##################

# Used to denote that no index exists in the main item list.
NO_ITEM_ELEMENT_INDEX = -1

##########################
# LOCATION KEY CONSTANTS #
##########################

LOCATION_ID_KEY = "location_id"
LOCATION_REQUIREMENTS = "requirements"
LOCATION_ROOM_KEY = "location_room"

##################################
# LOCATION REQUIREMENT CONSTANTS #
##################################

LOCATION_REQUIREMENT_TYPE_ROOM_COUNT = "room_count"
LOCATION_REQUIREMENT_TYPE_HAS_ALL_ROOMS = "has_all_rooms"
LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ALL = "has_items_all"
LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ANY = "has_items_any"
LOCATION_REQUIREMENT_TYPE_HAS_ITEM_COUNTS = "has_item_counts"
LOCATION_REQUIREMENT_TYPE_HAS_REGIONS_ACCESS = "has_regions_access"
LOCATION_REQUIREMENT_TYPE_HAS_LOCATIONS_ACCESS = "has_locations_access"
LOCATION_REQUIREMENT_TYPE_COUNT_LOCATIONS_ACCESS = "count_locations_access"

#####################
# CONTROL CONSTANTS #
#####################

# Enable room logic, when set to true, allows the rooms to be loaded into the world as items to be found.
# When false, "all rooms" will be available to the player "at the start"
ENABLE_ROOM_LOGIC = True

########################
# ROOM LOGIC POSITIONS #
########################

# Advance means going up that associated edge.
# Retreat means going down that edge.
# Edge creep means going up OR down that edge.
# Edge Pierce means going INTO the edge from non-edge.
# STANDALONE ARRAY (Outer Room)
# Tier:  Center Tier 1 is ranks 2-3 Center Tier 2 is 4-6 Center Tier 3 is 7-8 (Tier does not matter for Corner or Front.)
# Front Is Rank 1
# Back Is Rank 9
# Gems is Requires Gems
# North Pierce - Rank 9 from rank 8
# South Pierce - Rank 1 from Rank 2
# Frontback - Rare Front
#


ROOM_PICK_POSITION_CENTER_TIER_1 = "CENTER - Tier 1"
ROOM_PICK_POSITION_CENTER_TIER_1_GEMS = "CENTER - Tier 1 G"
ROOM_PICK_POSITION_CENTER_TIER_1_FOUNDATION = "CENTER - Tier 1 Foundation"
ROOM_PICK_POSITION_CENTER_TIER_2 = "CENTER - Tier 2"
ROOM_PICK_POSITION_CENTER_TIER_2_GEMS = "CENTER - Tier 2 G"
ROOM_PICK_POSITION_CENTER_TIER_3 = "CENTER - Tier 3"
ROOM_PICK_POSITION_CENTER_TIER_3_GEMS = "CENTER - Tier 3 G"
ROOM_PICK_POSITION_CENTER_RARE = "Center Rare"
ROOM_PICK_POSITION_CENTER_RARE_GEMS = "Center Rare G"
ROOM_PICK_POSITION_CORNER_RARE = "CORNER - RARE"
ROOM_PICK_POSITION_CORNER_RARE_GEMS = "CORNER - RARE G"
ROOM_PICK_POSITION_CORNER = "CORNER - Tier 1"
ROOM_PICK_POSITION_CORNER_GEMS = "CORNER - Tier 1 G"
ROOM_PICK_POSITION_EDGE_ADVANCE_EAST_WING_GEMS = "EDGE ADVANCE EASTWING - G"
ROOM_PICK_POSITION_EDGE_ADVANCE_WEST_WING_GEMS = "EDGE ADVANCE WESTWING - G"
ROOM_PICK_POSITION_EDGE_RETREAT_EAST_WING_GEMS = "EDGE RETREAT EASTWING - G"
ROOM_PICK_POSITION_EDGE_RETREAT_WEST_WING_GEMS = "EDGE RETREAT WESTWING - G"
ROOM_PICK_POSITION_EDGE_CREEP_RARE = "EDGECREEP - RARE"
ROOM_PICK_POSITION_EDGE_CREEP_RARE_GEMS = "EDGECREEP - RARE G"
ROOM_PICK_POSITION_EDGE_CREEP_EAST = "EDGECREEP EAST"
ROOM_PICK_POSITION_EDGE_CREEP_WEST = "EDGECREEP WEST"
ROOM_PICK_POSITION_EDGE_PIERCE_EAST = "EDGEPIERCE EAST"
ROOM_PICK_POSITION_EDGE_PIERCE_WEST = "EDGEPIERCE WEST"
ROOM_PICK_POSITION_EDGE_PIERCE_GEMS = "EDGEPIERCE G"
ROOM_PICK_POSITION_EDGE_PIERCE_RARE = "EDGEPIERCE - RARE"
ROOM_PICK_POSITION_EDGE_PIERCE_RARE_GEMS = "EDGEPIERCE - RARE G"
ROOM_PICK_POSITION_FRONT = "FRONT - Tier 1"
ROOM_PICK_POSITION_FRONT_GEMS = "FRONT - Tier 1 G"
ROOM_PICK_POSITION_FRONT_BACK_RARE = "FRONTBACK - RARE"
ROOM_PICK_POSITION_FRONT_BACK_RARE_GEMS = "FRONTBACK G - RARE"
ROOM_PICK_POSITION_NORTH_PIERCE = "NORTH PIERCE"
ROOM_PICK_POSITION_NORTH_PIERCE_GEMS = "NORTH PIERCE G"
ROOM_PICK_POSITION_SOUTH_PIERCE = "SOUTH PIERCE"
ROOM_PICK_POSITION_STANDALONE = "STANDALONE ARRAY"
ROOM_PICK_POSITION_STANDALONE_FULL = "STANDALONE ARRAY FULL"
ROOM_PICK_POSITION_ANTECHAMBER = "ANTECHAMBER"

N, E, S, W = 1, 2, 4, 8

DIRS = {
    N: (0, 1),
    E: (1, 0),
    S: (0, -1),
    W: (-1, 0),
}

OPPOSITE = {
    N: S,
    S: N,
    E: W,
    W: E,
}

POSITION_MINIMUM_PIECES = {
    ROOM_PICK_POSITION_CENTER_TIER_1: [(0, 0, 0, 0)], # Should always be true
    ROOM_PICK_POSITION_CENTER_TIER_1_GEMS: [(0, 0, 0, 0)], # Should always be true
    ROOM_PICK_POSITION_CENTER_TIER_1_FOUNDATION: [
        (0, 0, 0, 3),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
        (1, 0, 0, 0),
    ],
    ROOM_PICK_POSITION_CENTER_TIER_2: [
        (0, 0, 0, 4),
        (0, 0, 1, 3),
        (0, 0, 2, 0),
        (0, 1, 0, 3),
        (0, 1, 1, 0),
        (0, 2, 0, 0),
        (1, 0, 0, 3),
        (1, 0, 1, 0),
        (1, 1, 0, 0),
    ],
    ROOM_PICK_POSITION_CENTER_TIER_2_GEMS: [
        (0, 0, 0, 4),
        (0, 0, 1, 3),
        (0, 0, 2, 0),
        (0, 1, 0, 3),
        (0, 1, 1, 0),
        (0, 2, 0, 0),
        (1, 0, 0, 3),
        (1, 0, 1, 0),
        (1, 1, 0, 0),
    ],
    ROOM_PICK_POSITION_CENTER_TIER_3: [
        (0, 0, 0, 11),
        (0, 0, 1, 8),
        (0, 0, 2, 7),
        (0, 0, 3, 4),
        (0, 0, 4, 3),
        (0, 0, 5, 0),
        (0, 1, 0, 8),
        (0, 1, 1, 7),
        (0, 1, 2, 4),
        (0, 1, 3, 3),
        (0, 1, 4, 0),
        (0, 2, 0, 7),
        (0, 2, 1, 4),
        (0, 2, 2, 3),
        (0, 2, 3, 0),
        (0, 3, 0, 4),
        (0, 3, 1, 3),
        (0, 3, 2, 0),
        (0, 4, 0, 3),
        (0, 4, 1, 0),
        (0, 5, 0, 0),
        (1, 0, 0, 8),
        (1, 0, 1, 7),
        (1, 0, 2, 4),
        (1, 0, 3, 3),
        (1, 0, 4, 0),
        (1, 1, 0, 7),
        (1, 1, 1, 4),
        (1, 1, 2, 3),
        (1, 1, 3, 0),
        (1, 2, 0, 4),
        (1, 2, 1, 3),
        (1, 2, 2, 0),
        (1, 3, 0, 3),
        (1, 3, 1, 0),
        (1, 4, 0, 0),
        (2, 0, 0, 7),
        (2, 0, 1, 4),
        (2, 0, 2, 3),
        (2, 0, 3, 0),
        (2, 1, 0, 4),
        (2, 1, 1, 3),
        (2, 1, 2, 0),
        (2, 2, 0, 3),
        (2, 2, 1, 0),
        (2, 3, 0, 0),
        (3, 0, 0, 4),
        (3, 0, 1, 3),
        (3, 0, 2, 0),
        (3, 1, 0, 3),
        (3, 1, 1, 0),
        (3, 2, 0, 0),
        (4, 0, 0, 3),
        (4, 0, 1, 0),
        (4, 1, 0, 0),
        (5, 0, 0, 0),
    ],
    ROOM_PICK_POSITION_CENTER_TIER_3_GEMS: [
        (0, 0, 0, 11),
        (0, 0, 1, 8),
        (0, 0, 2, 7),
        (0, 0, 3, 4),
        (0, 0, 4, 3),
        (0, 0, 5, 0),
        (0, 1, 0, 8),
        (0, 1, 1, 7),
        (0, 1, 2, 4),
        (0, 1, 3, 3),
        (0, 1, 4, 0),
        (0, 2, 0, 7),
        (0, 2, 1, 4),
        (0, 2, 2, 3),
        (0, 2, 3, 0),
        (0, 3, 0, 4),
        (0, 3, 1, 3),
        (0, 3, 2, 0),
        (0, 4, 0, 3),
        (0, 4, 1, 0),
        (0, 5, 0, 0),
        (1, 0, 0, 8),
        (1, 0, 1, 7),
        (1, 0, 2, 4),
        (1, 0, 3, 3),
        (1, 0, 4, 0),
        (1, 1, 0, 7),
        (1, 1, 1, 4),
        (1, 1, 2, 3),
        (1, 1, 3, 0),
        (1, 2, 0, 4),
        (1, 2, 1, 3),
        (1, 2, 2, 0),
        (1, 3, 0, 3),
        (1, 3, 1, 0),
        (1, 4, 0, 0),
        (2, 0, 0, 7),
        (2, 0, 1, 4),
        (2, 0, 2, 3),
        (2, 0, 3, 0),
        (2, 1, 0, 4),
        (2, 1, 1, 3),
        (2, 1, 2, 0),
        (2, 2, 0, 3),
        (2, 2, 1, 0),
        (2, 3, 0, 0),
        (3, 0, 0, 4),
        (3, 0, 1, 3),
        (3, 0, 2, 0),
        (3, 1, 0, 3),
        (3, 1, 1, 0),
        (3, 2, 0, 0),
        (4, 0, 0, 3),
        (4, 0, 1, 0),
        (4, 1, 0, 0),
        (5, 0, 0, 0),
    ],
    ROOM_PICK_POSITION_CORNER: [
        (0, 0, 0, 3),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
        (1, 0, 0, 2),
        (2, 0, 0, 1),
    ],
    ROOM_PICK_POSITION_CORNER_GEMS: [
        (0, 0, 0, 3),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
        (1, 0, 0, 2),
        (2, 0, 0, 1),
    ],
    ROOM_PICK_POSITION_CORNER_RARE: [
        (0, 0, 0, 3),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
        (1, 0, 0, 2),
        (2, 0, 0, 1),
    ],
    ROOM_PICK_POSITION_CORNER_RARE_GEMS: [
        (0, 0, 0, 3),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
        (1, 0, 0, 2),
        (2, 0, 0, 1),
    ],
    ROOM_PICK_POSITION_EDGE_ADVANCE_EAST_WING_GEMS: [
        (0, 0, 0, 4),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (1, 0, 0, 3),
        (2, 0, 0, 2),
    ],
    ROOM_PICK_POSITION_EDGE_ADVANCE_WEST_WING_GEMS: [
        (0, 0, 0, 4),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (1, 0, 0, 3),
        (2, 0, 0, 2),
    ],
    ROOM_PICK_POSITION_EDGE_RETREAT_EAST_WING_GEMS: [
        (0, 0, 0, 4),
        (0, 0, 1, 3),
        (0, 0, 2, 2),
        (0, 1, 0, 3),
        (0, 1, 1, 2),
        (0, 1, 2, 1),
        (0, 2, 0, 2),
        (0, 2, 1, 1),
        (0, 3, 0, 1),
        (1, 0, 0, 3),
        (1, 0, 1, 2),
        (1, 0, 2, 1),
        (1, 1, 0, 2),
        (1, 1, 1, 1),
        (1, 2, 0, 1),
        (2, 0, 0, 2),
        (2, 0, 1, 1),
        (2, 1, 0, 1),
        (3, 0, 0, 1),
    ],
    ROOM_PICK_POSITION_EDGE_RETREAT_WEST_WING_GEMS: [
        (0, 0, 0, 4),
        (0, 0, 1, 3),
        (0, 0, 2, 2),
        (0, 1, 0, 3),
        (0, 1, 1, 2),
        (0, 1, 2, 1),
        (0, 2, 0, 2),
        (0, 2, 1, 1),
        (0, 3, 0, 1),
        (1, 0, 0, 3),
        (1, 0, 1, 2),
        (1, 0, 2, 1),
        (1, 1, 0, 2),
        (1, 1, 1, 1),
        (1, 2, 0, 1),
        (2, 0, 0, 2),
        (2, 0, 1, 1),
        (2, 1, 0, 1),
        (3, 0, 0, 1),
    ],
    ROOM_PICK_POSITION_EDGE_CREEP_RARE: [
        (0, 0, 0, 4),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (1, 0, 0, 3),
        (2, 0, 0, 2),
        (3, 0, 0, 1),
    ],
    ROOM_PICK_POSITION_EDGE_CREEP_RARE_GEMS: [
        (0, 0, 0, 4),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (1, 0, 0, 3),
        (2, 0, 0, 2),
        (3, 0, 0, 1),
    ],
    ROOM_PICK_POSITION_EDGE_CREEP_EAST: [
        (0, 0, 0, 4),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (1, 0, 0, 3),
        (2, 0, 0, 2),
        (3, 0, 0, 1),
    ],
    ROOM_PICK_POSITION_EDGE_CREEP_WEST: [
        (0, 0, 0, 4),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (1, 0, 0, 3),
        (2, 0, 0, 2),
        (3, 0, 0, 1),
    ],
    ROOM_PICK_POSITION_EDGE_PIERCE_EAST: [
        (0, 0, 0, 2),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
        (0, 2, 0, 0),
        (1, 0, 0, 1),
        (1, 0, 1, 0),
        (1, 1, 0, 0),
        (2, 0, 0, 0),
    ],
    ROOM_PICK_POSITION_EDGE_PIERCE_WEST: [
        (0, 0, 0, 2),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
        (0, 2, 0, 0),
        (1, 0, 0, 1),
        (1, 0, 1, 0),
        (1, 1, 0, 0),
        (2, 0, 0, 0),
    ],
    ROOM_PICK_POSITION_EDGE_PIERCE_GEMS: [
        (0, 0, 0, 2),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
        (0, 2, 0, 0),
        (1, 0, 0, 1),
        (1, 0, 1, 0),
        (1, 1, 0, 0),
        (2, 0, 0, 0),
    ],
    ROOM_PICK_POSITION_EDGE_PIERCE_RARE: [
        (0, 0, 0, 2),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
        (0, 2, 0, 0),
        (1, 0, 0, 1),
        (1, 0, 1, 0),
        (1, 1, 0, 0),
        (2, 0, 0, 0),
    ],
    ROOM_PICK_POSITION_EDGE_PIERCE_RARE_GEMS: [
        (0, 0, 0, 2),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
        (0, 2, 0, 0),
        (1, 0, 0, 1),
        (1, 0, 1, 0),
        (1, 1, 0, 0),
        (2, 0, 0, 0),
    ],
    ROOM_PICK_POSITION_FRONT: [(0, 0, 0, 0)], # should always be true
    ROOM_PICK_POSITION_FRONT_GEMS: [(0, 0, 0, 0)], # should always be true
    ROOM_PICK_POSITION_FRONT_BACK_RARE: [(0, 0, 0, 0)], # should always be true
    ROOM_PICK_POSITION_FRONT_BACK_RARE_GEMS: [(0, 0, 0, 0)], # should always be true
    ROOM_PICK_POSITION_NORTH_PIERCE: [
        (0, 0, 0, 14),
        (0, 0, 1, 13),
        (0, 0, 2, 10),
        (0, 0, 3, 9),
        (0, 0, 4, 6),
        (0, 0, 5, 5),
        (0, 0, 6, 2),
        (0, 0, 7, 1),
        (0, 1, 0, 13),
        (0, 1, 1, 10),
        (0, 1, 2, 9),
        (0, 1, 3, 6),
        (0, 1, 4, 5),
        (0, 1, 5, 2),
        (0, 1, 6, 1),
        (0, 1, 7, 0),
        (0, 2, 0, 10),
        (0, 2, 1, 9),
        (0, 2, 2, 6),
        (0, 2, 3, 5),
        (0, 2, 4, 2),
        (0, 2, 5, 1),
        (0, 2, 6, 0),
        (0, 3, 0, 9),
        (0, 3, 1, 6),
        (0, 3, 2, 5),
        (0, 3, 3, 2),
        (0, 3, 4, 1),
        (0, 3, 5, 0),
        (0, 4, 0, 6),
        (0, 4, 1, 5),
        (0, 4, 2, 2),
        (0, 4, 3, 1),
        (0, 4, 4, 0),
        (0, 5, 0, 5),
        (0, 5, 1, 2),
        (0, 5, 2, 1),
        (0, 5, 3, 0),
        (0, 6, 0, 2),
        (0, 6, 1, 1),
        (0, 6, 2, 0),
        (0, 7, 0, 1),
        (0, 7, 1, 0),
        (0, 8, 0, 0),
        (1, 0, 0, 13),
        (1, 0, 1, 10),
        (1, 0, 2, 9),
        (1, 0, 3, 6),
        (1, 0, 4, 5),
        (1, 0, 5, 2),
        (1, 0, 6, 1),
        (1, 1, 0, 10),
        (1, 1, 1, 9),
        (1, 1, 2, 6),
        (1, 1, 3, 5),
        (1, 1, 4, 2),
        (1, 1, 5, 1),
        (1, 1, 6, 0),
        (1, 2, 0, 9),
        (1, 2, 1, 6),
        (1, 2, 2, 5),
        (1, 2, 3, 2),
        (1, 2, 4, 1),
        (1, 2, 5, 0),
        (1, 3, 0, 6),
        (1, 3, 1, 5),
        (1, 3, 2, 2),
        (1, 3, 3, 1),
        (1, 3, 4, 0),
        (1, 4, 0, 5),
        (1, 4, 1, 2),
        (1, 4, 2, 1),
        (1, 4, 3, 0),
        (1, 5, 0, 2),
        (1, 5, 1, 1),
        (1, 5, 2, 0),
        (1, 6, 0, 1),
        (1, 6, 1, 0),
        (1, 7, 0, 0),
        (2, 0, 0, 10),
        (2, 0, 1, 9),
        (2, 0, 2, 6),
        (2, 0, 3, 5),
        (2, 0, 4, 2),
        (2, 0, 5, 1),
        (2, 0, 6, 0),
        (2, 1, 0, 9),
        (2, 1, 1, 6),
        (2, 1, 2, 5),
        (2, 1, 3, 2),
        (2, 1, 4, 1),
        (2, 1, 5, 0),
        (2, 2, 0, 6),
        (2, 2, 1, 5),
        (2, 2, 2, 2),
        (2, 2, 3, 1),
        (2, 2, 4, 0),
        (2, 3, 0, 5),
        (2, 3, 1, 2),
        (2, 3, 2, 1),
        (2, 3, 3, 0),
        (2, 4, 0, 2),
        (2, 4, 1, 1),
        (2, 4, 2, 0),
        (2, 5, 0, 1),
        (2, 5, 1, 0),
        (2, 6, 0, 0),
        (3, 0, 0, 9),
        (3, 0, 1, 6),
        (3, 0, 2, 5),
        (3, 0, 3, 2),
        (3, 0, 4, 1),
        (3, 0, 5, 0),
        (3, 1, 0, 6),
        (3, 1, 1, 5),
        (3, 1, 2, 2),
        (3, 1, 3, 1),
        (3, 1, 4, 0),
        (3, 2, 0, 5),
        (3, 2, 1, 2),
        (3, 2, 2, 1),
        (3, 2, 3, 0),
        (3, 3, 0, 2),
        (3, 3, 1, 1),
        (3, 3, 2, 0),
        (3, 4, 0, 1),
        (3, 4, 1, 0),
        (3, 5, 0, 0),
        (4, 0, 0, 6),
        (4, 0, 1, 5),
        (4, 0, 2, 2),
        (4, 0, 3, 1),
        (4, 0, 4, 0),
        (4, 1, 0, 5),
        (4, 1, 1, 2),
        (4, 1, 2, 1),
        (4, 1, 3, 0),
        (4, 2, 0, 2),
        (4, 2, 1, 1),
        (4, 2, 2, 0),
        (4, 3, 0, 1),
        (4, 3, 1, 0),
        (4, 4, 0, 0),
        (5, 0, 0, 5),
        (5, 0, 1, 2),
        (5, 0, 2, 1),
        (5, 0, 3, 0),
        (5, 1, 0, 2),
        (5, 1, 1, 1),
        (5, 1, 2, 0),
        (5, 2, 0, 1),
        (5, 2, 1, 0),
        (5, 3, 0, 0),
        (6, 0, 0, 2),
        (6, 0, 1, 1),
        (6, 0, 2, 0),
        (6, 1, 0, 1),
        (6, 1, 1, 0),
        (6, 2, 0, 0),
        (7, 0, 0, 1),
        (7, 0, 1, 0),
        (7, 1, 0, 0),
        (8, 0, 0, 0),
    ],
    ROOM_PICK_POSITION_NORTH_PIERCE_GEMS: [
        (0, 0, 0, 14),
        (0, 0, 1, 13),
        (0, 0, 2, 10),
        (0, 0, 3, 9),
        (0, 0, 4, 6),
        (0, 0, 5, 5),
        (0, 0, 6, 2),
        (0, 0, 7, 1),
        (0, 1, 0, 13),
        (0, 1, 1, 10),
        (0, 1, 2, 9),
        (0, 1, 3, 6),
        (0, 1, 4, 5),
        (0, 1, 5, 2),
        (0, 1, 6, 1),
        (0, 1, 7, 0),
        (0, 2, 0, 10),
        (0, 2, 1, 9),
        (0, 2, 2, 6),
        (0, 2, 3, 5),
        (0, 2, 4, 2),
        (0, 2, 5, 1),
        (0, 2, 6, 0),
        (0, 3, 0, 9),
        (0, 3, 1, 6),
        (0, 3, 2, 5),
        (0, 3, 3, 2),
        (0, 3, 4, 1),
        (0, 3, 5, 0),
        (0, 4, 0, 6),
        (0, 4, 1, 5),
        (0, 4, 2, 2),
        (0, 4, 3, 1),
        (0, 4, 4, 0),
        (0, 5, 0, 5),
        (0, 5, 1, 2),
        (0, 5, 2, 1),
        (0, 5, 3, 0),
        (0, 6, 0, 2),
        (0, 6, 1, 1),
        (0, 6, 2, 0),
        (0, 7, 0, 1),
        (0, 7, 1, 0),
        (0, 8, 0, 0),
        (1, 0, 0, 13),
        (1, 0, 1, 10),
        (1, 0, 2, 9),
        (1, 0, 3, 6),
        (1, 0, 4, 5),
        (1, 0, 5, 2),
        (1, 0, 6, 1),
        (1, 1, 0, 10),
        (1, 1, 1, 9),
        (1, 1, 2, 6),
        (1, 1, 3, 5),
        (1, 1, 4, 2),
        (1, 1, 5, 1),
        (1, 1, 6, 0),
        (1, 2, 0, 9),
        (1, 2, 1, 6),
        (1, 2, 2, 5),
        (1, 2, 3, 2),
        (1, 2, 4, 1),
        (1, 2, 5, 0),
        (1, 3, 0, 6),
        (1, 3, 1, 5),
        (1, 3, 2, 2),
        (1, 3, 3, 1),
        (1, 3, 4, 0),
        (1, 4, 0, 5),
        (1, 4, 1, 2),
        (1, 4, 2, 1),
        (1, 4, 3, 0),
        (1, 5, 0, 2),
        (1, 5, 1, 1),
        (1, 5, 2, 0),
        (1, 6, 0, 1),
        (1, 6, 1, 0),
        (1, 7, 0, 0),
        (2, 0, 0, 10),
        (2, 0, 1, 9),
        (2, 0, 2, 6),
        (2, 0, 3, 5),
        (2, 0, 4, 2),
        (2, 0, 5, 1),
        (2, 0, 6, 0),
        (2, 1, 0, 9),
        (2, 1, 1, 6),
        (2, 1, 2, 5),
        (2, 1, 3, 2),
        (2, 1, 4, 1),
        (2, 1, 5, 0),
        (2, 2, 0, 6),
        (2, 2, 1, 5),
        (2, 2, 2, 2),
        (2, 2, 3, 1),
        (2, 2, 4, 0),
        (2, 3, 0, 5),
        (2, 3, 1, 2),
        (2, 3, 2, 1),
        (2, 3, 3, 0),
        (2, 4, 0, 2),
        (2, 4, 1, 1),
        (2, 4, 2, 0),
        (2, 5, 0, 1),
        (2, 5, 1, 0),
        (2, 6, 0, 0),
        (3, 0, 0, 9),
        (3, 0, 1, 6),
        (3, 0, 2, 5),
        (3, 0, 3, 2),
        (3, 0, 4, 1),
        (3, 0, 5, 0),
        (3, 1, 0, 6),
        (3, 1, 1, 5),
        (3, 1, 2, 2),
        (3, 1, 3, 1),
        (3, 1, 4, 0),
        (3, 2, 0, 5),
        (3, 2, 1, 2),
        (3, 2, 2, 1),
        (3, 2, 3, 0),
        (3, 3, 0, 2),
        (3, 3, 1, 1),
        (3, 3, 2, 0),
        (3, 4, 0, 1),
        (3, 4, 1, 0),
        (3, 5, 0, 0),
        (4, 0, 0, 6),
        (4, 0, 1, 5),
        (4, 0, 2, 2),
        (4, 0, 3, 1),
        (4, 0, 4, 0),
        (4, 1, 0, 5),
        (4, 1, 1, 2),
        (4, 1, 2, 1),
        (4, 1, 3, 0),
        (4, 2, 0, 2),
        (4, 2, 1, 1),
        (4, 2, 2, 0),
        (4, 3, 0, 1),
        (4, 3, 1, 0),
        (4, 4, 0, 0),
        (5, 0, 0, 5),
        (5, 0, 1, 2),
        (5, 0, 2, 1),
        (5, 0, 3, 0),
        (5, 1, 0, 2),
        (5, 1, 1, 1),
        (5, 1, 2, 0),
        (5, 2, 0, 1),
        (5, 2, 1, 0),
        (5, 3, 0, 0),
        (6, 0, 0, 2),
        (6, 0, 1, 1),
        (6, 0, 2, 0),
        (6, 1, 0, 1),
        (6, 1, 1, 0),
        (6, 2, 0, 0),
        (7, 0, 0, 1),
        (7, 0, 1, 0),
        (7, 1, 0, 0),
        (8, 0, 0, 0),
    ],
    ROOM_PICK_POSITION_SOUTH_PIERCE: [
        (0, 0, 0, 2),
        (0, 1, 0, 1),
        (0, 2, 0, 0),
        (1, 0, 0, 1),
        (1, 1, 0, 0),
        (2, 0, 0, 0),
    ],
    ROOM_PICK_POSITION_ANTECHAMBER: [
        (0, 0, 0, 15),
        (0, 0, 1, 12),
        (0, 0, 2, 11),
        (0, 0, 3, 8),
        (0, 0, 4, 7),
        (0, 0, 5, 4),
        (0, 0, 6, 3),
        (0, 0, 7, 0),
        (0, 1, 0, 12),
        (0, 1, 1, 11),
        (0, 1, 2, 8),
        (0, 1, 3, 7),
        (0, 1, 4, 4),
        (0, 1, 5, 3),
        (0, 1, 6, 0),
        (0, 2, 0, 11),
        (0, 2, 1, 8),
        (0, 2, 2, 7),
        (0, 2, 3, 4),
        (0, 2, 4, 3),
        (0, 2, 5, 0),
        (0, 3, 0, 8),
        (0, 3, 1, 7),
        (0, 3, 2, 4),
        (0, 3, 3, 3),
        (0, 3, 4, 0),
        (0, 4, 0, 7),
        (0, 4, 1, 4),
        (0, 4, 2, 3),
        (0, 4, 3, 0),
        (0, 5, 0, 4),
        (0, 5, 1, 3),
        (0, 5, 2, 0),
        (0, 6, 0, 3),
        (0, 6, 1, 0),
        (0, 7, 0, 0),
        (1, 0, 0, 12),
        (1, 0, 1, 11),
        (1, 0, 2, 8),
        (1, 0, 3, 7),
        (1, 0, 4, 4),
        (1, 0, 5, 3),
        (1, 0, 6, 0),
        (1, 1, 0, 11),
        (1, 1, 1, 8),
        (1, 1, 2, 7),
        (1, 1, 3, 4),
        (1, 1, 4, 3),
        (1, 1, 5, 0),
        (1, 2, 0, 8),
        (1, 2, 1, 7),
        (1, 2, 2, 4),
        (1, 2, 3, 3),
        (1, 2, 4, 0),
        (1, 3, 0, 7),
        (1, 3, 1, 4),
        (1, 3, 2, 3),
        (1, 3, 3, 0),
        (1, 4, 0, 4),
        (1, 4, 1, 3),
        (1, 4, 2, 0),
        (1, 5, 0, 3),
        (1, 5, 1, 0),
        (1, 6, 0, 0),
        (2, 0, 0, 11),
        (2, 0, 1, 8),
        (2, 0, 2, 7),
        (2, 0, 3, 4),
        (2, 0, 4, 3),
        (2, 0, 5, 0),
        (2, 1, 0, 8),
        (2, 1, 1, 7),
        (2, 1, 2, 4),
        (2, 1, 3, 3),
        (2, 1, 4, 0),
        (2, 2, 0, 7),
        (2, 2, 1, 4),
        (2, 2, 2, 3),
        (2, 2, 3, 0),
        (2, 3, 0, 4),
        (2, 3, 1, 3),
        (2, 3, 2, 0),
        (2, 4, 0, 3),
        (2, 4, 1, 0),
        (2, 5, 0, 0),
        (3, 0, 0, 8),
        (3, 0, 1, 7),
        (3, 0, 2, 4),
        (3, 0, 3, 3),
        (3, 0, 4, 0),
        (3, 1, 0, 7),
        (3, 1, 1, 4),
        (3, 1, 2, 3),
        (3, 1, 3, 0),
        (3, 2, 0, 4),
        (3, 2, 1, 3),
        (3, 2, 2, 0),
        (3, 3, 0, 3),
        (3, 3, 1, 0),
        (3, 4, 0, 0),
        (4, 0, 0, 7),
        (4, 0, 1, 4),
        (4, 0, 2, 3),
        (4, 0, 3, 0),
        (4, 1, 0, 4),
        (4, 1, 1, 3),
        (4, 1, 2, 0),
        (4, 2, 0, 3),
        (4, 2, 1, 0),
        (4, 3, 0, 0),
        (5, 0, 0, 4),
        (5, 0, 1, 3),
        (5, 0, 2, 0),
        (5, 1, 0, 3),
        (5, 1, 1, 0),
        (5, 2, 0, 0),
        (6, 0, 0, 3),
        (6, 0, 1, 0),
        (6, 1, 0, 0),
        (7, 0, 0, 0),
    ]
}