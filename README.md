# Mining
Codes Which we use to Mine Data.

Code to Mine images from whole Internet of a Person or Thing or Anyone.
& Crop it from their Front of the Face.

How It Works.
First In Our Function We Will Paas three(3) Arguments.

1st=>Name of the Person + Keyword that who he is (To conifirm his identity)
example=>
act="Shahrukhan Khan"+"Bollywood Actor"

2nd=>Number of images you want to Download.
example=> 250

3rd=>Minimum Size of pic (90,90)

After passing those values in that function,Code will start his work.
it will download 250 images for you.

But
During this Downloading just like we experienced some times it will not gives 
that much amount of pics how much we defined in Arg.

So what code will do
it will download images 
after Download
it will Crop Those images from the Persons Face.
&
it will Count whole files
and
if images are less then defined argument then
Code will Delete whole folder of images.
and it will Download it again and start cropping it again.
and if again is less then again it will repeat same thing 
and for further proccess till it does not satisfy the 
given Arg value.

And in last to automate the full task we added a function 
which will read the excel sheet & will read every single name
by loop which we will define.
& Download all Names Which you Defined Their.
