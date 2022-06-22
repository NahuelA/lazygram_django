create post model
create profile model
  GLOSARY
- F: "Fix"
- C: "Complete"
- I: "Incomplete"
- A: "Add"
- //: "Verbose information"

##############
  To-do List
##############

********
  Home
********
  - Home view from show posts *C*
  - Show posts created by any user *I*
  - Like a posts *I*
  - Link to profile of the user who uploaded post *I*

*********
  Login
*********
  - Login view from sign in *C*
  - Password_change
  - Password_change_done
  - Password_reset
  - Password_reset_done
  - Password_reset_confirm
  - Password_reset_complete

  - Forgot your password? *I*
  - Validation change password *I*


***********
  Sign-up
***********
  - Sign up profile information *C* // Uploading pictures is not alowed *F*
  - Sign up from User view *C*
  - Edit request.POST data from UserSignUpView and ProfileSignUpView *C*
  - Use class is-invalid to border red in invalid field *I*
  - Use class invalid-feedback to create feedback invalid below field *I*

***********
  Profile
***********
  - List profile view *C*
  - Edit profile view *I*
  - Make a validation when change profile picture, if *I*
    a new image is detected, delete the old picture.
  - Create Posts *I*
  - Edit Posts *I*