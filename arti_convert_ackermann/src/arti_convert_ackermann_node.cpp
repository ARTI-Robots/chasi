/*
Created by clemens on 6/8/18.
This file is part of the software provided by ARTI
Copyright (c) 2018, ARTI
All rights reserved.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <arti_convert_ackermann/arti_convert_ackermann_node.h>

namespace arti_convert_ackermann
{
  ArtiConvertAckermannNode::ArtiConvertAckermannNode(ros::NodeHandle nh) : nh_(nh)
  {
    ackermann_sub_ = nh_.subscribe("/cmd_ackermann", 1, &ArtiConvertAckermannNode::ackermannCB, this);
    cmd_vel_pub_ = nh_.advertise<geometry_msgs::Twist>("/cmd_vel", 1);
  }

  void ArtiConvertAckermannNode::ackermannCB(const ackermann_msgs::AckermannDrive &msg)
  {
    geometry_msgs::Twist pub_msg;
    pub_msg.linear.x = msg.speed;
    pub_msg.angular.z = msg.steering_angle;

    cmd_vel_pub_.publish(pub_msg);
  }
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "arti_convert_ackermann_node");

  ros::NodeHandle nh("~");

  arti_convert_ackermann::ArtiConvertAckermannNode convert_node(nh);

  ros::spin();

  return 0;
}

