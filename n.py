Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import { Bell, Camera, Home, Image, Menu, MessageSquare, MoreHorizontal, Search, Smile, User } from "lucide-react"
import Link from "next/link"
import * as React from "react"

import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Separator } from "@/components/ui/separator"
import { Textarea } from "@/components/ui/textarea"

export default function Component() {
  const [postContent, setPostContent] = React.useState("")

  const handlePostSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    console.log("Submitting post:", postContent)
    setPostContent("")
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center h-16">
          <div className="flex items-center">
            <Link href="/" className="text-2xl font-bold text-blue-600">
              SocialApp
            </Link>
            <div className="ml-10 flex items-baseline space-x-4">
              <Link href="/" className="text-gray-500 hover:text-gray-900">
                <Home className="h-5 w-5" />
              </Link>
              <Link href="/messages" className="text-gray-500 hover:text-gray-900">
                <MessageSquare className="h-5 w-5" />
              </Link>
              <Link href="/notifications" className="text-gray-500 hover:text-gray-900">
                <Bell className="h-5 w-5" />
              </Link>
            </div>
          </div>
          <div className="flex items-center">
            <form className="mr-4">
              <Input className="w-64" placeholder="Search..." type="search" />
            </form>
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="ghost" className="relative h-8 w-8 rounded-full">
                  <Avatar className="h-8 w-8">
                    <AvatarImage alt="User avatar" src="/placeholder-avatar.jpg" />
                    <AvatarFallback>U</AvatarFallback>
                  </Avatar>
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent className="w-56" align="end" forceMount>
                <DropdownMenuLabel className="font-normal">
                  <div className="flex flex-col space-y-1">
                    <p className="text-sm font-medium leading-none">John Doe</p>
                    <p className="text-xs leading-none text-muted-foreground">john.doe@example.com</p>
                  </div>
                </DropdownMenuLabel>
                <DropdownMenuSeparator />
                <DropdownMenuItem>
                  <User className="mr-2 h-4 w-4" />
                  <span>Profile</span>
                </DropdownMenuItem>
                <DropdownMenuItem>
                  <MessageSquare className="mr-2 h-4 w-4" />
                  <span>Messages</span>
                </DropdownMenuItem>
                <DropdownMenuItem>
                  <Bell className="mr-2 h-4 w-4" />
                  <span>Notifications</span>
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem>Log out</DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </div>
      </header>
      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="flex space-x-4">
          <div className="w-2/3">
            <Card className="mb-6">
              <CardHeader>
                <div className="flex w-max space-x-4 p-4">
                  {Array.from({ length: 10 }).map((_, i) => (
                    <div key={i} className="w-32 text-center">
                      <Avatar className="w-20 h-20 mx-auto mb-2 ring-2 ring-blue-500 ring-offset-2">
                        <AvatarImage src={`/placeholder-avatar-${i + 1}.jpg`} alt={`User ${i + 1}`} />
                        <AvatarFallback>U{i + 1}</AvatarFallback>
                      </Avatar>
                      <p className="text-sm">User {i + 1}</p>
                    </div>
                  ))}
                </div>
              </CardHeader>
            </Card>
            <Card className="mb-6">
              <CardHeader>
                <form onSubmit={handlePostSubmit}>
                  <Textarea
                    placeholder="What's on your mind?"
                    value={postContent}
                    onChange={(e) => setPostContent(e.target.value)}
                    className="mb-2"
                  />
                  <div className="flex justify-between items-center">
                    <div className="flex space-x-2">
                      <Button type="button" variant="outline" size="sm">
                        <Image className="h-4 w-4 mr-2" />
                        Photo
                      </Button>
                      <Button type="button" variant="outline" size="sm">
                        <Camera className="h-4 w-4 mr-2" />
                        Video
                      </Button>
                      <Button type="button" variant="outline" size="sm">
                        <Smile className="h-4 w-4 mr-2" />
                        Emoji
                      </Button>
                    </div>
                    <Button type="submit">Post</Button>
                  </div>
                </form>
              </CardHeader>
            </Card>
            <div className="space-y-4">
              {[1, 2, 3].map((post) => (
                <Card key={post}>
                  <CardHeader className="flex items-center space-x-4">
                    <Avatar>
                      <AvatarImage alt={`User ${post}`} src={`/placeholder-avatar-${post}.jpg`} />
                      <AvatarFallback>U{post}</AvatarFallback>
                    </Avatar>
                    <div className="flex-1">
                      <div className="flex items-center justify-between">
                        <h3 className="text-lg font-semibold">User {post}</h3>
                        <Button variant="ghost" size="sm">
                          <MoreHorizontal className="h-4 w-4" />
                        </Button>
                      </div>
                      <p className="text-sm text-gray-500">2 hours ago</p>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <p>This is a sample post content. It can be much longer and include more details.</p>
                    <img
                      src={`/placeholder.svg?height=300&width=400`}
                      alt="Post image"
                      className="mt-4 rounded-lg w-full"
                    />
                  </CardContent>
                  <CardFooter className="flex justify-between">
                    <Button variant="ghost">
                      <Smile className="h-4 w-4 mr-2" />
                      Like
                    </Button>
                    <Button variant="ghost">
                      <MessageSquare className="h-4 w-4 mr-2" />
                      Comment
                    </Button>
                    <Button variant="ghost">Share</Button>
                  </CardFooter>
                </Card>
              ))}
            </div>
          </div>
          <div className="w-1/3 space-y-6">
            <Card>
              <CardHeader>
                <h3 className="text-lg font-semibold">Trending Topics</h3>
              </CardHeader>
              <CardContent>
...                 <div className="space-y-4">
...                   {["#TechNews", "#SocialMediaTrends", "#DigitalMarketing", "#WebDevelopment", "#AI"].map((topic) => (
...                     <div key={topic} className="flex items-center justify-between">
...                       <p className="font-medium">{topic}</p>
...                       <span className="text-sm text-gray-500">1.2K posts</span>
...                     </div>
...                   ))}
...                 </div>
...               </CardContent>
...             </Card>
...             <Card>
...               <CardHeader>
...                 <h3 className="text-lg font-semibold">Online Friends</h3>
...               </CardHeader>
...               <CardContent>
...                 <div className="space-y-4">
...                   {[1, 2, 3, 4, 5].map((friend) => (
...                     <div key={friend} className="flex items-center space-x-4">
...                       <Avatar>
...                         <AvatarImage alt={`Friend ${friend}`} src={`/placeholder-avatar-${friend + 5}.jpg`} />
...                         <AvatarFallback>F{friend}</AvatarFallback>
...                       </Avatar>
...                       <div>
...                         <h4 className="font-semibold">Friend {friend}</h4>
...                         <p className="text-sm text-green-500">Online</p>
...                       </div>
...                     </div>
...                   ))}
...                 </div>
...               </CardContent>
...             </Card>
...           </div>
...         </div>
...       </main>
...     </div>
...   )
