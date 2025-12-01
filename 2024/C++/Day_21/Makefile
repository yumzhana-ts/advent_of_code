NAME		=	Keypad_Conundrum

# Compiler
CPP			=	c++

# Compiler Flags
CPPFLAGS	=	-Wall -Werror -Wextra -std=c++98 -I. -Iinclude
RM 			= 	rm -rf

# Directories
OBJS_DIR 	= 	objs
SRC_DIRS 	= 	srcs

# Source and Object Files
SRCS 		= 	$(foreach dir,$(SRC_DIRS),$(wildcard $(dir)/*.cpp))
OBJS 		= 	$(SRCS:%.cpp=$(OBJS_DIR)/%.o)

all : $(OBJS_DIR) $(NAME)

# Compile and Link the Project
$(NAME) : $(OBJS)
	$(CPP) $(CPPFLAGS) $^ -o $@
	@echo "Compilation successful."


# Compile Source Files into Object Files
$(OBJS_DIR)/%.o: %.cpp | $(OBJS_DIR)
	@mkdir -p $(@D)
	$(CPP) $(CPPFLAGS) -c $< -o $@

# Create the Object File Directory
$(OBJS_DIR):
	@mkdir -p $(OBJS_DIR)/$(SRC_DIRS)

# Clean Objects and Executable
clean :
	$(RM) $(OBJS_DIR)
	@echo "Object files and directory cleaned."

fclean : clean
	$(RM) $(NAME)
	@echo "Executable removed."


.PHONY : clean fclean re all bonus