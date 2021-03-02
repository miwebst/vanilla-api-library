module.exports = async function (context, req) {
  context.res = {
    // status: 200, /* Defaults to 200 */
    body: { text: "Node GetMessage 2020-08-28 11:53" },
  };
};
