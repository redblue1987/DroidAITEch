project( DisplayImage )
find_package( OpenCV REQUIRED )
add_executable( DisplayImage DisplayImage )
target_link_libraries( DisplayImage ${OpenCV_LIBS} )

